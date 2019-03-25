from node import Node
import heapq
import utils_a as ut
def manhattan(statePosition, goalPosition):
    return abs(statePosition[0] - goalPosition[0]) + abs(statePosition[1] - goalPosition[1])

class aStartrue:

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


    def truedist(self, position):

        node = ut.Aetoil(self.initState, position, self.wallStates, self.rowsize, self.colsize)
        while node.father != None:
            node = node.father
        return node.cost

