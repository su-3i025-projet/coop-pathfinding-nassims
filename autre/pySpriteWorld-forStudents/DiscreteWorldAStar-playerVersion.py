# -*- coding: utf-8 -*-

# Nicolas, 2015-11-18

from __future__ import absolute_import, print_function, unicode_literals
from gameclass import Game,check_init_game_done
from spritebuilder import SpriteBuilder
from players import Player
from sprite import MovingSprite
from ontology import Ontology
from itertools import chain
import pygame
import glo
from noeud import Noeud
import heapq
import random 
import numpy as np
import sys


# ---- ---- ---- ---- ---- ----
# ---- Misc                ----
# ---- ---- ---- ---- ---- ----




# ---- ---- ---- ---- ---- ----
# ---- Main                ----
# ---- ---- ---- ---- ---- ----
def manhattan(statePosition, goalPosition):
    return abs(statePosition[0] - goalPosition[0]) + abs(statePosition[1] - goalPosition[1])

game = Game()

def init(_boardname=None):
    global player,game
    name = _boardname if _boardname is not None else 'pathfindingWorld3'
    game = Game('Cartes/' + name + '.json', SpriteBuilder)
    game.O = Ontology(True, 'SpriteSheet-32x32/tiny_spritesheet_ontology.csv')
    game.populate_sprite_names(game.O)
    game.fps = 5  # frames per second
    game.mainiteration()
    player = game.player
    
def main():

    #for arg in sys.argv:
    iterations = 100 # default
    if len(sys.argv) == 2:
        iterations = int(sys.argv[1])
    print ("Iterations: ")
    print (iterations)

    init()
    

    
    #-------------------------------
    # Building the matrix
    #-------------------------------
       
           
    # on localise tous les états initiaux (loc du joueur)
    initStates = [o.get_rowcol() for o in game.layers['joueur']]
    print ("Init states:", initStates)
    
    # on localise tous les objets ramassables
    goalStates = [o.get_rowcol() for o in game.layers['ramassable']]
    print ("Goal states:", goalStates)
        
    # on localise tous les murs
    wallStates = [w.get_rowcol() for w in game.layers['obstacle']]
    #print ("Wall states:", wallStates)
        
    
    #-------------------------------
    # Building the best path with A*
    #-------------------------------
    noeudInitial = Noeud(list(initStates[0]), 0, None)
    frontiere = [(noeudInitial.cost + manhattan(noeudInitial.position, goalStates[0]), noeudInitial)]
    reserve = {}
    noeudCourant = noeudInitial

    while frontiere != [] and not noeudCourant.position == goalStates[0]:
        (min_f, noeudCourant) = heapq.heappop(frontiere)
        if noeudCourant.position == list(goalStates[0]):
            break
        next_row = noeudCourant.position[0]
        next_col = noeudCourant.position[1]
        if ((next_row,
             next_col) not in wallStates) and next_row >= 0 and next_row <= 20 and next_col >= 0 and next_col <= 20:
            if noeudCourant.identifiantNoeud() not in reserve:
                reserve[noeudCourant.identifiantNoeud()] = noeudCourant.cost
                nouveauxNoeuds = noeudCourant.expand()
                for noeud in nouveauxNoeuds:
                    f = noeud.cost + manhattan(noeud.position, goalStates[0])
                    heapq.heappush(frontiere, (f, noeud))

    
    
        
    #-------------------------------
    # Moving along the path
    #-------------------------------
        
    # bon ici on fait juste un random walker pour exemple...
    

    row,col = initStates[0]
    #row2,col2 = (5,5)

    """for i in range(iterations):
    
    
        x_inc,y_inc = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        next_row = row+x_inc
        next_col = col+y_inc
        if ((next_row,next_col) not in wallStates) and next_row>=0 and next_row<=20 and next_col>=0 and next_col<=20:
            player.set_rowcol(next_row,next_col)
            print ("pos 1:",next_row,next_col)
            game.mainiteration()

            col=next_col
            row=next_row
"""
    moves = []
    while noeudCourant != None:
        moves.insert(0, [noeudCourant.position[0], noeudCourant.position[1]])
        noeudCourant = noeudCourant.father
    for i in moves:
        player.set_rowcol(i[0], i[1])
        game.mainiteration()


        # si on a  trouvé l'objet on le ramasse
        if (row,col)==goalStates[0]:
            o = game.player.ramasse(game.layers)
            game.mainiteration()
            print ("Objet trouvé!", o)
            break
        '''
        #x,y = game.player.get_pos()
    
        '''

    pygame.quit()
    
        
    
   

if __name__ == '__main__':
    main()
    


