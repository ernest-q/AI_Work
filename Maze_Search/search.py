import argparse
import os.path
from os import path
from queue import PriorityQueue
from queue import Queue

class Node:
    def __init__(self, cargo=None, parent=None, child=None):
        self.cargo = cargo
        self.parent = parent
        self.child = child
    
    def __str__(self):
        return str(self.cargo)

    def getCargo(self):
        return self.cargo

    def getParent(self):
        return self.parent

def mazeToArray(fileSelect):

    file = open("{}".format(fileSelect),"r")
    contents = file.read()

    splitMaze = contents.split("\n")
    for i in range(len(splitMaze)):
        mazeArray = []
    for i in range(len(splitMaze)):
        innerMaze = []
        for x in range(len(splitMaze[i])):
            
            innerMaze.append(splitMaze[i][x])
        mazeArray.append(innerMaze)
    
    return mazeArray

def printMaze(maze):
    for i in range(len(maze)):
            print()
            for x in range(len(maze[i])):
                print(maze[i][x],end="")
                

def getStartPos(maze):
    for i in range(len(maze)):
            for x in range(len(maze[i])):
                if maze[i][x] == "P":
                    start = (i,x)
    
    return start

def getGoalPos(maze):
    for i in range(len(maze)):
            for x in range(len(maze[i])):
                if maze[i][x] == ".":
                    goal = (i,x)
                
    return goal

def returnPath(maze,start,goal):
    print("here")
    path = []
    finished = False
    goalX, goalY = start
    x,y = goal
    path.insert(0,(x,y))
    while(not finished):
        #yah = input("continue?")
        if (x,y) == (goalX,goalY):
            maze[goalX][goalY] = "."
            printMaze(maze)
            return path
        else:
            if maze[x][y] == "^":
                maze[x][y] = " "
                x,y = (x-1,y)
                path.insert(0,(x-1,y))
                printMaze(maze)
            if maze[x][y] == "<":
                maze[x][y] = " "
                x,y = (x,y-1)
                path.insert(0,(x-1,y))
                printMaze(maze)
            if maze[x][y] == "v":
                maze[x][y] = " "
                x,y = (x+1,y)
                path.insert(0,(x-1,y))
                printMaze(maze)
            if maze[x][y] == ">":
                maze[x][y] = " "
                x,y = (x,y+1)
                path.insert(0,(x-1,y))
                printMaze(maze)
    
    print("Path Cost: {}".format(len(path)))

def calcManDistance(startX,startY,goalX,goalY):
    manhatDist = abs(startX - goalX) + abs(startY - goalY)
    return manhatDist

def greedSearch(maze):

    success = False
    start = getStartPos(maze)
    goal = getGoalPos(maze)
    goalx, goaly = goal
    x,y = start
    pq = PriorityQueue()
    pq.put((1,(x,y)))

    """ SO IT DOESN'T GO INTO INFINITE LOOP LIKE IT SHOULD"""
    visited = []

    """UP,LEFT,DOWN,RIGHT"""
    printMaze(maze)
    print(pq.empty())
    while(not success):

        yah = input("continue?")
        h, cords = pq.get()
        print(pq.empty())
        while(not pq.empty()):
            pq.get()
        x, y = cords
        visited.append((x,y))
        print(x,y)

        maze[x][y] = "+"
        if h == 0:
            success = True
        else:
            if maze[x-1][y] == " " or maze[x-1][y] == "+":
                heuristic = calcManDistance(x-1,y,goalx,goaly)
                pq.put((heuristic,(x-1,y)))

            if maze[x][y-1] == " " or maze[x][y-1] == "+":
                heuristic = calcManDistance(x,y-1,goalx,goaly)
                pq.put((heuristic,(x,y-1)))
                
            if maze[x+1][y] == " " or maze[x+1][y] == "+":
                heuristic = calcManDistance(x+1,y,goalx,goaly)
                pq.put((heuristic,(x+1,y)))
                
            if maze[x][y+1] == " " or maze[x][y+1] == " " "+":
                heuristic = calcManDistance(x,y+1,goalx,goaly)
                pq.put((heuristic,(x,y+1)))
                
        printMaze(maze)

    return 0

def aStarSearch(maze):

    success = False
    start = getStartPos(maze)
    goal = getGoalPos(maze)
    goalx, goaly = goal
    x,y = start
    pq = PriorityQueue()
    """Added, the 0 at the end """
    pq.put((1,0,(x,y)))

    visited = []

    while not success:
        #yah = input("continue?")
        h,sp, cords = pq.get()
        x, y = cords
        visited.append((x,y))

        if (x,y) == (goalx,goaly):
            break
        if h == 0:
            success = True
            break
        else:
            if maze[x-1][y] == " " or maze[x-1][y] == ".":
                """manD = calcManDistance(x-1,y,goalx,goaly)
                stepCost = (int(maze[x][y])+1)
                maze[x-1][y] = "{}".format(stepCost)
                h = manD + stepCost
                pq.put((h,(x-1,y)))
                printMaze(maze)"""
                manD = calcManDistance(x-1,y,goalx,goaly)
                stepCost = (sp+1)
                maze[x-1][y] = "v"
                h = manD + stepCost
                pq.put((h,stepCost,(x-1,y)))
                printMaze(maze)

            if maze[x][y-1] == " " or maze[x][y-1] == ".":
                """manD = calcManDistance(x,y-1,goalx,goaly)
                stepCost = (int(maze[x][y])+1)
                maze[x][y-1] = "{}".format(stepCost)
                h = manD + stepCost
                pq.put((h,(x,y-1)))
                printMaze(maze)"""
                manD = calcManDistance(x,y-1,goalx,goaly)
                stepCost = (sp+1)
                maze[x][y-1] = ">"
                h = manD + stepCost
                pq.put((h,stepCost,(x,y-1)))
                printMaze(maze)
                
            if maze[x+1][y] == " " or maze[x+1][y] == ".":
                """manD = calcManDistance(x+1,y,goalx,goaly)
                stepCost = (int(maze[x][y])+1)
                maze[x+1][y] = "{}".format(stepCost)
                h = manD + stepCost
                pq.put((h,(x+1,y)))
                printMaze(maze)"""
                manD = calcManDistance(x+1,y,goalx,goaly)
                stepCost = (sp+1)
                maze[x+1][y] = "^"
                h = manD + stepCost
                pq.put((h,stepCost,(x+1,y)))
                printMaze(maze)
                
            if maze[x][y+1] == " " or maze[x][y+1] == ".":
                """manD = calcManDistance(x,y+1,goalx,goaly)
                stepCost = (int(maze[x][y])+1)
                maze[x][y+1] = "{}".format(stepCost)
                h = manD + stepCost
                pq.put((h,(x,y+1)))
                printMaze(maze)"""
                manD = calcManDistance(x,y+1,goalx,goaly)
                stepCost = (sp+1)
                maze[x][y+1] = "<"
                h = manD + stepCost
                pq.put((h,stepCost,(x,y+1)))
                printMaze(maze)

    print(returnPath(maze,start,goal))    
            
    return 0

def checkAdj(maze,x,y,visited):
    up = False
    left = False
    down = False
    right = False

    if maze[x-1][y] != "%" and (x-1,y) not in visited:
        up = True
    if maze[x][y-1] != "%" and (x,y-1) not in visited:
        left = True
    if maze [x+1][y] != "%" and (x+1,y) not in visited:
        down = True
    if maze [x][y+1] != "%" and (x,y+1) not in visited:
        right = True

    return up,left,down,right


def betterbreadth(maze):

    start = getStartPos(maze)
    goal = getGoalPos(maze)
    goalx, goaly = goal
    x,y = start

    root = Node((x,y))
    frontier = []
    frontier.append(root)
    visited = []

    while frontier:
        root = frontier.pop(0)

        x,y = root.getCargo()
        if (x,y) == (goalx,goaly):
            break
        print(x,y)
        up,left,down,right = checkAdj(maze,x,y,visited)
        print(up,left,down,right)
        visited.append((x,y))
        if up:
            newNode1 = Node((x-1,y),root)
            frontier.append(newNode1)
        if left:
            newNode2 = Node((x,y-1),root)
            frontier.append(newNode2)
        if down:
            newNode3 = Node((x+1,y),root)
            frontier.append(newNode3)
        if right:
            newNode4 = Node((x,y+1),root)
            frontier.append(newNode4)
        
    while root.getParent() != None:
        print(root.getCargo())
        x,y = root.getCargo()
        maze[x][y] = "O"
        root = root.parent
    
    printMaze(maze)

def betterDepthNode(maze):

    start = getStartPos(maze)
    goal = getGoalPos(maze)
    goalx, goaly = goal
    x,y = start

    root = Node((x,y))
    stack = []
    stack.append(root)
    visited = []

    while stack:
        root = stack.pop()

        x,y = root.getCargo()
        if (x,y) == (goalx,goaly):
            break
        print(x,y)
        up,left,down,right = checkAdj(maze,x,y,visited)
        print(up,left,down,right)
        visited.append((x,y))
        
        if right:
            newNode4 = Node((x,y+1),root)
            stack.append(newNode4)
        if down:
            newNode3 = Node((x+1,y),root)
            stack.append(newNode3)
        if left:
            newNode2 = Node((x,y-1),root)
            stack.append(newNode2)
        if up:
            newNode1 = Node((x-1,y),root)
            stack.append(newNode1)
    
    while root.getParent() != None:
        print(root.getCargo())
        x,y = root.getCargo()
        maze[x][y] = "O"
        root = root.parent
    
    printMaze(maze)

    for i in range(len(visited)):
        x,y = visited[i]
        maze[x][y] = "X"

    printMaze(maze)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--method", help="method")
    parser.add_argument("maze", help="maze.txt")
    
    args = parser.parse_args()
    fileName = args.maze
    if path.exists(fileName):

        theMaze = mazeToArray(fileName)
       
        if args.method == "depth":
            betterDepthNode(theMaze)

        elif args.method == "breadth":
            betterbreadth(theMaze)

        elif args.method == "greedy":
            greedSearch(theMaze)
            
        elif args.method == "astar":
            aStarSearch(theMaze)
        else:
            print("Invalid operation")
            exit()
    else:
        print("Invalid file name")

if __name__ == "__main__":
    main()