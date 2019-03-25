from node import Node
import heapq
def manhattan(statePosition, goalPosition):
    return abs(statePosition[0] - goalPosition[0]) + abs(statePosition[1] - goalPosition[1])

def Aetoil(initState, goalState, wallStates, rowsize, colsize):

    initialNode = Node((initState), 0, None)
    goalStates = goalState
    border = [(initialNode.cost + manhattan(initialNode.position, goalStates), initialNode)]
    reserve = {}
    currentNode = initialNode


    while border != [] and not currentNode.position == goalStates:
        #print("border ",border)

        (min_f, currentNode) = heapq.heappop(border)
        if currentNode.position == goalStates:
            break
        next_row = currentNode.position[0]
        next_col = currentNode.position[1]
        #print(next_row, next_col)
        if ((next_row,
             next_col) not in wallStates) and next_row >= 0 and next_row < rowsize and next_col >= 0 and next_col < colsize:
            #print("sahit")
            if currentNode.identifiantNoeud() not in reserve:
                reserve[currentNode.identifiantNoeud()] = currentNode.cost
                newNode = currentNode.expand()
                #print("new node ", newNode)
                #print("sahit")
                for node in newNode:

                    f = node.cost + manhattan(node.position, goalStates)
                    heapq.heappush(border, (f, node))
        #print(currentNode.position == goalStates)

    return currentNode