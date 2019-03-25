import copy
class Node:

    def __init__(self, position, cost, father, time = 0):
        self.position = position
        self.cost = cost
        self.father = father
        self.time = time

    def trace(self):
        """ affiche tous les ancetres du noeud
            """
        moves = []
        currentNode = self
        while currentNode != None:
            moves.insert(0, [currentNode.position[0], currentNode.position[1]])
            currentNode = currentNode.father
        return moves

    def identifiantNoeud(self):
        return str(self.position[0]) + "," + str(self.position[1])

    def __lt__(self, other):
        return self.identifiantNoeud() < other.identifiantNoeud()

    def expand(self):
        nouveauxNoeuds = []
        c = copy.copy(self.position)
        c[0] = c[0] + 1
        nouveauxNoeuds.append(Node(c, self.cost + 1, self))
        c = copy.copy(self.position)
        c[0] = c[0] - 1
        nouveauxNoeuds.append(Node(c, self.cost + 1, self))
        c = copy.copy(self.position)
        c[1] = c[1] + 1
        nouveauxNoeuds.append(Node(c, self.cost + 1, self))
        c = copy.copy(self.position)
        c[1] = c[1] - 1
        nouveauxNoeuds.append(Node(c, self.cost + 1, self))

        return nouveauxNoeuds

    def __repr__(self):
        return  str(self.position)



    def expandT(self):
        nouveauxNoeuds = []
        c = copy.copy(self.position)
        c[0] = c[0] + 1
        nouveauxNoeuds.append(Node(c, self.cost + 1, self, self.time+1))
        c = copy.copy(self.position)
        c[0] = c[0] - 1
        nouveauxNoeuds.append(Node(c, self.cost + 1, self, self.time+1))
        c = copy.copy(self.position)
        c[1] = c[1] + 1
        nouveauxNoeuds.append(Node(c, self.cost + 1, self, self.time+1))
        c = copy.copy(self.position)
        c[1] = c[1] - 1
        nouveauxNoeuds.append(Node(c, self.cost + 1, self, self.time+1))
        c = copy.copy(self.position)
        nouveauxNoeuds.append(Node(c, self.cost, self, self.time+1))

        return nouveauxNoeuds