class Groupe:

    """

    Class that represents a group of players that can move at the same time without collision

    """

    def __init__(self):
        self.caseList = []
        self.playersList = []

    def add(self, player):

        """
            Adds a player to the group

        :param player: PlayerPath object

        """

        self.playersList.append(player)
        self.caseList = list(list(i) for i in set(tuple(i) for i in self.caseList) | set(tuple(i) for i in player.path))

    def compare(self, player):

        """

            Tests if there is an intersection between the player's path and the path of the other players of the group

        :param player:

        :return: bool
                True if there is an intersection, False otherwise

        """

        for i in player.path:
            if i in self.caseList:
                return True
        return False

    def startMoving(self):

        """

            Changes the attribute move of all players of the group to True, so they can move

        """

        for player in self.playersList:
            player.move = True

    def stopMoving(self):

        """

        Changes the attribute move of all players of the group to False, so they cant move

        """

        for player in self.playersList:
            player.move = False

    def nextMove(self):

        """

        :return: dict of lists
                the next move of all players of the group

        """

        moves = {}
        for player in self.playersList:
            moves[player.number] = player.movee()
        return moves

    def atGoal(self):

        """

            Tests if all players are on their goal

        :return:
                True if all players are on their goal False otherwise

        """

        for player in self.playersList:
            if not player.onGoal():
                return False
        return True