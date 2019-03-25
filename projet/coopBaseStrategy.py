
from groupe import Groupe
from strategy import Strategy
class CoopBaseStrategy(Strategy):

    """

        Class that represents Cooperative Basic Strategy

    """

    def __init__(self, players, game):

        """

        :param players:

        :param game:

        """
        super().__init__(players, game)
        self.index = 0
        # split in groups
        self.groups = []
        self.split()

        for i in range(1,len(self.groups)):
            self.groups[i].stopMoving()

    def nextIteration(self):

        """

            returns the next move of all players only one group can move at a time

        :return: list of lists
                the next move of all players

        """

        #if all players of one groups are at their goal state we start moving the next group
        if self.groups[self.index].atGoal():

            self.groups[self.index].stopMoving()

            self.index += 1
            if self.index == len(self.groups):
                #done
                return None
            # changement de path
            g = []

            for player in self.groups[self.index -1].playersList:
                g.append(player.goalState)
                self.players.remove(player)

            for player in self.players:
                player.walls += g
            self.split()
            self.groups[self.index].startMoving()



        return self.groups[self.index].nextMove()

    def split(self):

        """

        Splits the players into groups

        """
        #f chek
        self.index = 0
        self.groups = []
        for joueur in self.players:


            for i in range(len(self.groups) + 1):
                #if end of list of groups

                if i == len(self.groups) :
                    newGroupe = Groupe()
                    newGroupe.add(joueur)
                    self.groups.append(newGroupe)
                    break

                if not self.groups[i].compare(joueur):
                    self.groups[i].add(joueur)
                    break

        self.groups[0].startMoving()
