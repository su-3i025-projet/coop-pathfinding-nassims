# -*- coding: utf-8 -*-



from __future__ import absolute_import, print_function, unicode_literals

import random
import sys

import pygame
from gameclass import Game
from ontology import Ontology
from playerPath import PlayerPath
from spritebuilder import SpriteBuilder
from coopBaseStrategy import CoopBaseStrategy

# ---- ---- ---- ---- ---- ----
# ---- Main                ----
# ---- ---- ---- ---- ---- ----



game = Game()


def init(_boardname=None):
    global player, game
    # pathfindingWorld_MultiPlayer4
    name = _boardname if _boardname is not None else 'at2'
    game = Game('Cartes/' + name + '.json', SpriteBuilder)
    game.O = Ontology(True, 'SpriteSheet-32x32/tiny_spritesheet_ontology.csv')
    game.populate_sprite_names(game.O)
    game.fps = 5  # frames per second
    game.mainiteration()
    game.mask.allow_overlaping_players = True
    # player = game.player


def main():
    # for arg in sys.argv:
    iterations = 150  # default
    if len(sys.argv) == 2:
        iterations = int(sys.argv[1])
    print("Iterations: ")
    print(iterations)

    init()

    # -------------------------------
    # Initialisation
    # -------------------------------

    players = [o for o in game.layers['joueur']]
    nbPlayers = len(players)


    # on localise tous les états initiaux (loc du joueur)
    initStates = [o.get_rowcol() for o in game.layers['joueur']]
    print("Init states:", initStates)

    # on localise tous les objets ramassables
    goalStates = [o.get_rowcol() for o in game.layers['ramassable']]
    print("Goal states:", goalStates)

    # on localise tous les murs
    wallStates = [w.get_rowcol() for w in game.layers['obstacle']]
    # print ("Wall states:", wallStates)


    print(game.layers['ramassable'])

    initStates = [o.get_rowcol() for o in game.layers['joueur']]
    print("Init states:", initStates)

    # on localise tous les objets ramassables
    goalStates = [o.get_rowcol() for o in game.layers['ramassable']]
    print("Goal states:", goalStates)
    goalStates[0], goalStates[1] = goalStates[1], goalStates[0]


    pathPlayersList = []
    for i in range(len(players)):
        pathPlayersList.append(PlayerPath(i, list(initStates[i]), list(goalStates[i]), wallStates, game))

    baseStrat = CoopBaseStrategy(pathPlayersList, game)
    print(baseStrat.groups)
    nbIteration = 0
    while not baseStrat.onGoals():
        nextMoves = baseStrat.nextIteration()
        for key, value in nextMoves.items():
            players[key].set_rowcol(value[0], value[1])
        nbIteration += 1
        game.mainiteration()

    pygame.quit()
    print("done in ", nbIteration)

if __name__ == '__main__':
    main()



