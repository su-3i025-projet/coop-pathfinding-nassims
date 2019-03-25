import utils_a as ut
from strategy import Strategy

class PathSlicingStrategy(Strategy):

    """

        Class that represents Path Slicing Strategy

    """

    def __init__(self, players, game):

        """

        :param players:
                list of players (playerPath object)
        :param game:
                the game (the map with all informations like the walls...)
        """

        super().__init__(players, game)

    def nextIteration(self):#TODO comms

        """

            Methode that returns the next move of all the players
            if there is a colision it makes the changes

        :return:
                list of lists that represents the next move of the players

        """

        done = False
        while not done:
            done = True
            for j in range(self.nbPlayers):
                # test colision
                if self.testColision(self.players[j]):
                    self.newPath(self.players[j])
                    done = False
        # je cree une liste avec les next sur chaque joueur

        moves = {}
        for x in self.players:

            moves[x.number] = x.movee()
        return moves



    def testColision(self, player):

        """
            Tests if there is a collision between the player in  parameters and all other
            players

        :param player:
                playerPath object that contains the path of the player

        :return:
                True if there is a collision False otherwise

        """

        for j in range(self.nbPlayers):
            if not player == self.players[j]:
                nextMovePlayer1 = player.getNext()
                nextMovePlayer2 = self.players[j].getNext()
                previousMovePlayer1 = player.getPrevious()
                previousMovePlayer2 = self.players[j].getPrevious()
                if previousMovePlayer1 is not None and previousMovePlayer2 is not None:

                    if nextMovePlayer1[0] == nextMovePlayer2[0] and nextMovePlayer1[1] == nextMovePlayer2[1]:
                        return True

                    if self.players[j].canMove() and nextMovePlayer1[0] == previousMovePlayer2[0] and nextMovePlayer1[1] == previousMovePlayer2[1] and previousMovePlayer1[0] == nextMovePlayer2[0] and previousMovePlayer1[1] == nextMovePlayer2[1]:
                        return True
                return False

    def newPath(self, player):

        """

            Creates a new path for the player in parameters
            by calculating the new path using A star Algorithm from the player's next move
            and his second next move

        :param player:
                playerPath object that contains the path of the player

        """

        newWalls = player.walls
        next = player.getNext()
        newWalls.append((next[0], next[1]))
        new = ut.Aetoil(player.getPrevious(), player.path[player.index+1], newWalls ,self.game.spriteBuilder.rowsize, self.game.spriteBuilder.colsize).trace()
        player.removeNextMove()
        player.removeNextMove()
        player.insertNewPath(new)

