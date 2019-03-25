from node import Node
import heapq
import utils_a as ut
def manhattan(statePosition, goalPosition):
    return abs(statePosition[0] - goalPosition[0]) + abs(statePosition[1] - goalPosition[1])

class aStar:

    def __init__(self, initState, goalState, wallStates, rowsize, colsize):

        self.initState= initState
        self.initialNode = Node(initState,0,None)
        self.goalState = goalState
        self.border = [(self.initialNode.cost + manhattan(self.initialNode.position, self.goalState), self.initialNode)]
        self.reserve = {}
        self.currentNode = self.initialNode
        self.wallStates = wallStates
        self.rowsize = rowsize
        self.colsize = colsize

    def run(self):

        while self.border != [] and not self.currentNode.position == self.goalState:
            (min_f, self.currentNode) = heapq.heappop(self.border)
            if self.currentNode.position == self.goalState:
                self.reserve[self.currentNode.identifiantNoeud()] = self.currentNode.cost
                break
            next_row = self.currentNode.position[0]
            next_col = self.currentNode.position[1]

            if (next_row, next_col) not in self.wallStates and next_row >= 0 and next_row < self.rowsize and next_col >= 0 and next_col < self.colsize:

                if self.currentNode.identifiantNoeud() not in self.reserve:

                    self.reserve[self.currentNode.identifiantNoeud()] = self.currentNode.cost
                    newNode = self.currentNode.expand()

                    for node in newNode:
                        f = node.cost + manhattan(node.position, self.goalState)
                        heapq.heappush(self.border, (f, node))


        return self.currentNode

    def truedist(self, position):

        """for key,value in self.reserve.items():
            if key == str(position[0])+','+str(position[1]):
                return value

        self.goalState = position
        self.run()
        print(self.reserve)
        return self.reserve[str(position[0]) + ',' + str(position[1])]"""

        node = ut.Aetoil(self.initState, position, self.wallStates, self.rowsize, self.colsize)
        while node.father != None:
            node = node.father
        return node.cost

