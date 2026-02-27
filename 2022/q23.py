import sys

class cell:
    def __init__(self, isStart, isEnd, adjacencyList):
        self.adjacent_cells = adjacencyList
        self.isStart = isStart
        self.isEnd = isEnd
        self.distance = None
    
    def getAdjacencyList(self):
        return self.adjacent_cells
    
    def isStart(self):
        return self.isStart
    
    def isEnd(self):
        return self.isEnd
    
    def setDistance(self, distance):
        self.distance = distance
    
    def getDistance(self):
        return self.distance

def calculateCellForColumn(height, start, end, x):
    y=0
    k=0
    while k < int(height-2):
        first_line = current_grid[k][start:end]
        second_line = current_grid[k+1][start:end]
        third_line = current_grid[k+2][start:end]
        
        isCurrentCellStart = False
        isCurrentCellEnd = False

        currentCellAdjacencyList = []

        print(first_line)
        print(second_line)
        print(third_line)
        print(x, y)

        #First Line
        if (first_line[1:3] == "  "):
            print("We know gap")
            currentCellAdjacencyList.append((x, y-1))
        elif (first_line[1:3] == "--"):
            print("WALLLLL")
        elif (first_line[1:3] == "vv"):
            print("Entrance")
            isCurrentCellStart = True
        elif (first_line[1:3] == "^^"):
            print("Exit")
            isCurrentCellEnd = True

        #Second Line - left side
        if (second_line[0] == " "):
            print("Gap second line")
            currentCellAdjacencyList.append((x-1, y))
        if (second_line[0] == "|"):
            print("Wall")
        if (second_line[0] == ">"):
            print("Entrance")
            isCurrentCellStart = True
        if (second_line[0] == "<"):
            print("Exit")
            isCurrentCellEnd = True

        #Second Line - right side
        if (second_line[3] == " "):
            print("Gap second line")
            currentCellAdjacencyList.append((x+1, y))
        if (second_line[3] == "|"):
            print("Wall")
        if (second_line[3] == ">"):
            print("Exit")
            isCurrentCellEnd = True
        if (second_line[3] == "<"):
            print("Entrance")
            isCurrentCellStart = True

        #Third Line
        if (third_line[1:3] == "  "):
            print("We know gap")
            currentCellAdjacencyList.append((x, y+1))
        elif (third_line[1:3] == "--"):
            print("WALLLLL")
        elif (third_line[1:3] == "vv"):
            print("Exit")
            isCurrentCellEnd = True
        elif (third_line[1:3] == "^^"):
            print("Entrance")
            isCurrentCellStart = True
        
        currentCell = cell(isCurrentCellStart, isCurrentCellEnd, currentCellAdjacencyList)

        cell_list[x][y] = currentCell

        y+=1
        k+=2

def getCellAdjacencyList(x, y):
    current_cell = cell_list[x][y]

    return current_cell.getAdjacencyList()

def getNext(current_cell, total_distance):
    list = current_cell.getAdjacencyList()
    for cell in list:
        (x, y) = cell
        adjacent_cell = cell_list[x][y]
        if (adjacent_cell.getDistance() == None):
            adjacent_cell.setDistance(total_distance + 1)
        else:
            if(adjacent_cell.getDistance() < total_distance):
                return


        adjacent = getCellAdjacencyList(x, y)
        #We have cell coords
        #Using that, find that cell's adjacency list
        #distance stuff

def solveForShortestPath():
    start_point = None
    end_point = None

    for x in cell_list:
        for y in cell_list[x]:
            if (cell_list[x][y].isStart()):
                start_point = cell_list[x][y]
            if (cell_list[x][y].isEnd()):
                end_point = cell_list[x][y]

    start_point.setDistance = 0
    total_distance = 0




cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    height, width = map(int, sys.stdin.readline().rstrip().split())

    current_grid = []
    for i in range(height):
        next_line = sys.stdin.readline().rstrip()
        current_grid.append(next_line)
    
    #for j in range(height): print(current_grid[j])

    cell_list = [[None] * int((height-1)/2) for _ in range(int(width/3))]

    for x in range(int(width/3)):
        calculateCellForColumn(height, 3 * x , 4 + 3 * x, x)

#0(in)-4(ex) is y=1
#3-7 is y=2
#6-10 is y=3
#9-13
