import utils_a as ut
from AStar import aStar
from astartdi import aStartrue

class PlayerPath:

    """

        Class that represents a player and the path that he will use to get the goal

    """

    def __init__(self ,number ,initState, goalState, wallStates, game):

        """

        :param number: int
                    number of the player in the players list
        :param initState: list
                    the initial position of the player
        :param goalState: list
                    the goal position of the player
        :param wallStates: list of lists
                    the walls position
        :param game: game object
                    the game (the map with all informations like the walls...)

        """
        self.initState = initState
        self.goalState = goalState
        self.number = number
        self.game = game
        self.index = 1
        self.astar = aStar(initState, goalState, wallStates, game.spriteBuilder.rowsize, game.spriteBuilder.colsize)
        self.path = (self.astar.run()).trace()
        self.move = True
        self.walls = wallStates
        self.astarForTrueDist = aStartrue(goalState, initState, wallStates, game.spriteBuilder.rowsize, game.spriteBuilder.colsize)


    def canMove(self):

        """
        tests of the player is at the goal state or not

        :return:
                False if the player is at the goal, True otherwise
        """

        if self.index == len(self.path):
            self.move = False
        return self.move


    def movee(self):

        """

        Moves a player if he can move

        :return: the next move of the player

        """

        #return the initial state if he cant move and he's in the initial state
        if not self.move and self.index == 0:
            return self.path[self.index]

        #return the goal state if he's at the goal state
        if self.index == len(self.path):
            return self.path[-1]

        #return the next move and increments the index attribute
        nextMove = self.path[self.index]
        self.index += 1

        return nextMove

    def getNext(self):

        """

        :return: the next move of the player

        """
        # if the player is at the goal state his next move will be to stay on that state
        if self.index == len(self.path):
            return self.path[-1]
        return self.path[self.index]

    def getPrevious(self):

        """

        :return: the previous move of the player or None if he's at his initial state

        """
        if self.index is 1:
            return None
        return self.path[self.index-1]

    def removeNextMove(self):

        """

        Removes the next move of the player

        """
        self.path.remove(self.path[self.index])

    def insertNewPath(self, newPath):

        """

        add the new path in the position the index attribute

        :param newPath: list of lists
                    the new path of the player

        """

        indice = self.index
        for state in newPath:
            self.path.insert(indice, state)
            indice += 1

    def onGoal(self):

        """

        Tests if the player is at his goal

        :return:
                True if the player is at his goal, False otherwise

        """
        return self.index == len(self.path)
