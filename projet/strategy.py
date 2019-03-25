from abc import ABC, abstractmethod

class Strategy(ABC):

    def __init__(self, players, game):
        self.game = game
        self.players = players  # qui on un parcours
        self.nbPlayers = len(self.players)

    @abstractmethod
    def nextIteration(self):
        pass

    def onGoals(self):

        """

            Tests if all players are on their goal

        :return:
                True if all players are on their goal False otherwise

        """

        for player in self.players:

            if not player.onGoal():
                return False

        return True