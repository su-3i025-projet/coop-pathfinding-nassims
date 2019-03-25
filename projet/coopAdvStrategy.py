from aStarTmp import AStarTmp
from strategy import Strategy

class CoopAdvStrategy(Strategy):

    def __init__(self,initStates,goalStates, players, wallStates, game):
        self.game = game
        self.players = players
        self.nbPlayers = len(self.players)
        self.astar = AStarTmp(initStates, wallStates, game.spriteBuilder.rowsize, game.spriteBuilder.colsize)
        for i in range(self.nbPlayers):
            self.players[i].path = self.astar.run(list(initStates[i]), list(goalStates[i]), self.players[i])




    def nextIteration(self):

        """

            Methode that returns the next move of all the players
            if there is a colision it makes the changes

        :return:
                list of lists that represents the next move of the players

        """

        moves = {}
        for x in self.players:

            moves[x.number] = x.movee()
        return moves
