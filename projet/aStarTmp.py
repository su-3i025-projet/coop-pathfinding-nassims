from node import Node
import heapq



class AStarTmp:
    def __init__(self,initStates, wallStates, rowsize, colsize):

        self.wallStates = wallStates
        self.rowsize = rowsize
        self.colsize = colsize
        self.inMove = []

    def run(self, initState, goalState, player):

        self.goalState = goalState
        self.initialNode = Node(initState, 0, None, 0)
        self.currentNode = self.initialNode
        self.border = [(self.initialNode.cost + player.astarForTrueDist.truedist(self.initialNode.position), self.initialNode)]

        self.reserve = {}
        self.currentNode = self.initialNode


        while self.border != [] and not self.currentNode.position == self.goalState:

            (min_f, self.currentNode) = heapq.heappop(self.border)

            if self.currentNode.position == self.goalState:

                break
            next_row = self.currentNode.position[0]
            next_col = self.currentNode.position[1]
            #ajouter teste temps

            if (next_row,
                next_col) not in self.wallStates and next_row >= 0 and next_row < self.rowsize and next_col >= 0 and next_col < self.colsize and self.testTemps(self.currentNode):

                if self.currentNode.identifiantNoeud() not in self.reserve:# existe mais avec un cost plus petit ?
                    self.reserve[self.currentNode.identifiantNoeud()] = self.currentNode.cost
                    newNode = self.currentNode.expandT()

                    for node in newNode:
                        if (node.position[0], node.position[1]) not in self.wallStates and node.position[0] >= 0 and node.position[0] < self.rowsize and node.position[1] >= 0 and node.position[1] < self.colsize:

                            f = node.cost + player.astarForTrueDist.truedist(node.position)

                            heapq.heappush(self.border, (f, node))

        moves = []
        currentNod = self.currentNode
        # add the player's moves in 'inMove'
        while currentNod != None:
            self.inMove.append((currentNod.position[0], currentNod.position[1], currentNod.time))
            moves.insert(0, [currentNod.position[0], currentNod.position[1]])
            currentNod = currentNod.father

        return moves



    def testTemps(self, node):

        if (node.position[0], node.position[1], node.time) in self.inMove:

            return False
        else:
            return True





