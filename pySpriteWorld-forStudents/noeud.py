import copy
class Noeud:
    def __init__(self, position, cost, father):
        self.position = position
        self.cost = cost
        self.father = father

    def trace(self):
        """ affiche tous les ancetres du noeud
            """
        n = self
        c = 0
        while n != None:
            print(n.identifiantNoeud())
            n = n.father
            c += 1
        print("Nombre d'étapes de la solution:", c - 1)
        return

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
        c[0] = c[0] - 11
        nouveauxNoeuds.append(Noeud(c, self.cost + 1, self))
        c = copy.copy(self.position)
        c[1] = c[1] + 1
        nouveauxNoeuds.append(Noeud(c, self.cost + 1, self))
        c = copy.copy(self.position)
        c[1] = c[1] - 1
        nouveauxNoeuds.append(Noeud(c, self.cost + 1, self))

        return nouveauxNoeuds