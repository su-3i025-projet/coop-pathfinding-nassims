from __future__ import absolute_import, print_function, unicode_literals

import random
import sys

import pygame
from gameclass import Game
from ontology import Ontology
from playerPath import PlayerPath
from spritebuilder import SpriteBuilder
from coopBaseStrategy import CoopBaseStrategy
from pathSlicingStrategy import PathSlicingStrategy
from coopAdvStrategy import CoopAdvStrategy


class initTest():

    def __init__(self,_boardname=None, swap = False, affiche = True):
        self.game = Game()
        name = _boardname if _boardname is not None else 'at2'
        self.game = Game('Cartes/' + name + '.json', SpriteBuilder)
        self.game.O = Ontology(True, 'SpriteSheet-32x32/tiny_spritesheet_ontology.csv')
        self.game.populate_sprite_names(self.game.O)
        self.game.fps = 2  # frames per second
        self.affiche = affiche
        if affiche:
            self.game.mainiteration()
        self.game.mask.allow_overlaping_players = True

        # player = game.player

        # on localise tous les états initiaux (loc du joueur)
        self.initStates = [o.get_rowcol() for o in self.game.layers['joueur']]
        print("Init states:", self.initStates)

        # on localise tous les objets ramassables
        self.goalStates = [o.get_rowcol() for o in self.game.layers['ramassable']]
        print("Goal states:", self.goalStates)

        # on localise tous les murs
        self.wallStates = [w.get_rowcol() for w in self.game.layers['obstacle']]
        # print ("Wall states:", self.wallStates)

        self.nbIteration = 0



        if swap:
            self.goalStates[0], self.goalStates[1] = self.goalStates[1], self.goalStates[0]

        self.players = [o for o in self.game.layers['joueur']]

    def placementAlea(self):

        # -------------------------------
        # Placement aleatoire des fioles de couleur
        # -------------------------------
        for o in self.game.layers['ramassable']:  # les rouges puis jaunes puis bleues
            # et on met la fiole qqpart au hasard
            x = random.randint(1, 19)
            y = random.randint(1, 19)
            while (x, y) in self.wallStates:
                x = random.randint(1, 19)
                y = random.randint(1, 19)
            o.set_rowcol(x, y)
            self.game.layers['ramassable'].add(o)
            self.game.mainiteration()

    def coopBaseStrategyTest(self):
        self.pathPlayersList = []
        for i in range(len(self.players)):
            self.pathPlayersList.append(PlayerPath(i, list(self.initStates[i]), list(self.goalStates[i]), self.wallStates, self.game))

        baseStrat = CoopBaseStrategy(self.pathPlayersList, self.game)
        self.nbIteration = 0
        while not baseStrat.onGoals():
            nextMoves = baseStrat.nextIteration()
            for key, value in nextMoves.items():
                self.players[key].set_rowcol(value[0], value[1])
            self.nbIteration += 1

            if self.affiche:
                self.game.mainiteration()

        pygame.quit()
        print("Cooperative Basic Strategy : done in ", self.nbIteration, " moves")

    def pathSlicingStrategyTest(self):
        self.pathPlayersList = []
        for i in range(len(self.players)):
            self.pathPlayersList.append(PlayerPath(i, list(self.initStates[i]), list(self.goalStates[i]), self.wallStates, self.game))


        pathsclicing = PathSlicingStrategy(self.pathPlayersList, self.game)
        self.nbIteration = 0
        while not pathsclicing.onGoals():
            nextMoves = pathsclicing.nextIteration()

            for key, value in nextMoves.items():
                self.players[key].set_rowcol(value[0], value[1])
            if self.affiche:
                self.game.mainiteration()

            self.nbIteration += 1

        pygame.quit()
        print("Path Slicing Strategy : done in ", self.nbIteration, " moves")

    def coopAdvStrategyTest(self):
        self.pathPlayersList = []
        for i in range(len(self.players)):
            self.pathPlayersList.append(PlayerPath(i, list(self.initStates[i]), list(self.goalStates[i]), self.wallStates, self.game))


        s = CoopAdvStrategy(list(self.initStates), list(self.goalStates), self.pathPlayersList, list(self.wallStates), self.game)
        self.nbIteration = 0
        while not s.onGoals():
            nextMoves = s.nextIteration()

            for key, value in nextMoves.items():
                self.players[key].set_rowcol(value[0], value[1])
            if self.affiche:
                self.game.mainiteration()
            self.nbIteration += 1

        pygame.quit()
        print("Cooperative Advanced Strategy : done in ", self.nbIteration, " moves")

def testAll(boardname, swap = False):
    test = initTest(boardname, swap , False)
    test.pathSlicingStrategyTest()
    print("====================================")
    test = initTest(boardname, swap, False)
    test.coopBaseStrategyTest()
    print("====================================")
    test = initTest(boardname, swap, False)
    test.coopAdvStrategy()

if __name__ == '__main__':
    m = initTest('carte11', True, True)
    #m.pathSlicingStrategyTest()
    #testAll("carte1")
    #m.coopBaseStrategyTest()
    #m.coopAdvStrategyTest()