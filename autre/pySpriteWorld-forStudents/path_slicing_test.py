# -*- coding: utf-8 -*-


from __future__ import absolute_import, print_function, unicode_literals

import random

import pygame
from gameclass import Game
from ontology import Ontology
from pathSlicingStrategy import PathSlicingStrategy
from playerPath import PlayerPath
from spritebuilder import SpriteBuilder
from AStar import aStar

# ---- ---- ---- ---- ---- ----
# ---- Main                ----
# ---- ---- ---- ---- ---- ----



game = Game()


def init(_boardname=None):
    global player, game

    name = _boardname if _boardname is not None else 'carte1'
    game = Game('Cartes/' + name + '.json', SpriteBuilder)
    game.O = Ontology(True, 'SpriteSheet-32x32/tiny_spritesheet_ontology.csv')
    game.populate_sprite_names(game.O)
    game.fps = 5 # frames per second
    game.mainiteration()
    game.mask.allow_overlaping_players = True
    # player = game.player

def placementAlea():

    # -------------------------------
    # Placement aleatoire des fioles de couleur
    # -------------------------------
    wallStates = [w.get_rowcol() for w in game.layers['obstacle']] #TODO: a mettre ou pas
    for o in game.layers['ramassable']:  # les rouges puis jaunes puis bleues
        # et on met la fiole qqpart au hasard
        x = random.randint(1, 19)
        y = random.randint(1, 19)
        while (x, y) in wallStates:
            x = random.randint(1, 19)
            y = random.randint(1, 19)
        o.set_rowcol(x, y)
        game.layers['ramassable'].add(o)
        game.mainiteration()

def swapGoals(goalStates):
    goalStates[0], goalStates[1] = goalStates[1], goalStates[0]


def pathSlicingTest():
    pathPlayersList = []

    for i in range(len(players)):
        pathPlayersList.append(PlayerPath(i, list(initStates[i]), list(goalStates[i]), wallStates, game))
        print(pathPlayersList[i].path)
        print('init ', initStates[i], " goal ", goalStates[i])

    pathsclicing = PathSlicingStrategy(pathPlayersList, game)
    nbIteration = 0
    while not pathsclicing.onGoals():
        nextMoves = pathsclicing.nextIteration()

        for key, value in nextMoves.items():
            players[key].set_rowcol(value[0], value[1])

        game.mainiteration()
        nbIteration += 1

    pygame.quit()
    print("done in ", nbIteration)

def main():

    init()

    # -------------------------------
    # Initialisation
    # -------------------------------

    players = [o for o in game.layers['joueur']]
    print(players)
    nbPlayers = len(players)
    score = [0] * nbPlayers

    # on localise tous les états initiaux (loc du joueur)
    initStates = [o.get_rowcol() for o in game.layers['joueur']]
    print("Init states:", initStates)

    # on localise tous les objets ramassables
    goalStates = [o.get_rowcol() for o in game.layers['ramassable']]

    goalStates[0], goalStates[1] = goalStates[1], goalStates[0]
    print("Goal states:", goalStates)
    # on localise tous les murs
    wallStates = [w.get_rowcol() for w in game.layers['obstacle']]
    # print ("Wall states:", wallStates)



    pathPlayersList = []

    for i in range(len(players)):
        pathPlayersList.append(PlayerPath(i, list(initStates[i]), list(goalStates[i]), wallStates, game))
        print(pathPlayersList[i].path)
        print('init ', initStates[i], " goal ", goalStates[i])

    pathsclicing = PathSlicingStrategy(pathPlayersList, game)
    nbIteration = 0
    while not pathsclicing.onGoals():
        nextMoves = pathsclicing.nextIteration()

        for key, value in nextMoves.items():
            players[key].set_rowcol(value[0], value[1])

        game.mainiteration()
        nbIteration += 1

    pygame.quit()
    print("done in ", nbIteration)





if __name__ == '__main__':
    main()


