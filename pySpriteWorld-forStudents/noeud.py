import copy
class Noeud:
    def __init__(self, position, cost, father):
        self.position = position
        self.cost = cost
        self.father = father

    def trace(self):
        """ affiche tous les ancetres du noeud
            """
        moves = []
        noeudCourant = self
        while noeudCourant != None:
            moves.insert(0, [noeudCourant.position[0], noeudCourant.position[1]])
            noeudCourant = noeudCourant.father
        return moves

    def identifiantNoeud(self):
        return str(self.position[0]) + "," + str(self.position[1])

    def __lt__(self, other):
        return self.identifiantNoeud() < other.identifiantNoeud()

    def expand(self):
        nouveauxNoeuds = []
        c = copy.copy(self.position)
        c[0] = c[0] + 1
        nouveauxNoeuds.append(Noeud(c, self.cost + 1, self))
        c = copy.copy(self.position)
        c[0] = c[0] - 1
        nouveauxNoeuds.append(Noeud(c, self.cost + 1, self))
        c = copy.copy(self.position)
        c[1] = c[1] + 1
        nouveauxNoeuds.append(Noeud(c, self.cost + 1, self))
        c = copy.copy(self.position)
        c[1] = c[1] - 1
        nouveauxNoeuds.append(Noeud(c, self.cost + 1, self))

        return nouveauxNoeuds