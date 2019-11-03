import argparse
import os.path
from os import path
from queue import PriorityQueue
from queue import Queue

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

def depthFirstSearch(maze):

    """FINISH ADDING THE SOLUTION COST """
    solutionCost = 0
    activePath = []
    success = False
    while(not success):
        #yah = input("continue?")

        """GETS THE START POSITION"""
        start = getStartPos(maze)
        print(start)
        x,y = start

        """GOAL TEST, POSSIBLY DO SEPERATE METHOD IF REPEATED"""
        if maze[x-1][y] == ".":
            maze[x-1][y] = "P"
            maze[x][y] = "+"
            activePath.append((x,y))
            solutionCost += 1
            print("SUCCESS")
            success = True
            break

        elif maze[x][y-1] == ".":
            maze[x][y-1] = "P"
            maze[x][y] = "+"
            activePath.append((x,y))
            solutionCost += 1
            print("SUCCESS")
            print(activePath)
            success = True
            break

        elif maze[x+1][y] == ".":
            maze[x+1][y] = "P"
            maze[x][y] = "+"
            activePath.append((x,y))
            solutionCost += 1
            print("SUCCESS")
            print(activePath)
            success = True
            break

        elif maze[x][y+1] == ".":
            maze[x][y+1] = "P"
            maze[x][y] = "+"
            activePath.append((x,y))
            solutionCost += 1
            print("SUCCESS")
            print(activePath)
            success = True
            break

        if maze[x-1][y] == " ":
            maze[x-1][y] = "P"
            maze[x][y] = "+"
            activePath.append((x,y))
            solutionCost += 1

        elif maze[x][y-1] == " ":
            maze[x][y-1] = "P"
            maze[x][y] = "+"
            activePath.append((x,y))
            solutionCost += 1
        
        elif maze[x+1][y] == " ":
            maze[x+1][y] = "P"
            maze[x][y] = "+"
            activePath.append((x,y))
            solutionCost += 1
        
        elif maze[x][y+1] == " ":
            maze[x][y+1] = "P"
            maze[x][y] = "+"
            activePath.append((x,y))
            solutionCost += 1

        else:
            if maze[x-1][y] == "+" and (x-1,y) == activePath[len(activePath)-1]:
                maze[x-1][y] = "P"
                maze[x][y] = "-"
                activePath.pop()

            elif maze[x][y-1] == "+" and (x,y-1) == activePath[len(activePath)-1]:
                maze[x][y-1] = "P"
                maze[x][y] = "-"
                activePath.pop()
            
            elif maze[x+1][y] == "+" and (x+1,y) == activePath[len(activePath)-1]:
                maze[x+1][y] = "P"
                maze[x][y] = "-"
                activePath.pop()
            
            elif maze[x][y+1] == "+" and (x,y+1) == activePath[len(activePath)-1]:
                maze[x][y+1] = "P"
                maze[x][y] = "-"
                activePath.pop()
        
        printMaze(maze)
        """print(activePath)"""

def returnPath(maze,start,goal):
    print("here")
    path = []
    finished = False
    goalX, goalY = start
    x,y = goal
    path.insert(0,(x,y))
    while(not finished):
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
    

def betterDepthFirst(maze):
    stack = []
    visited = []
    start = getStartPos(maze)
    x,y = start
    stack.append((x,y))
    success = False
    goal = getGoalPos(maze)
    hasAdj = True
    while(not success):
        yah = input("continue?")

        if stack != [] and hasAdj:
            x,y = stack.pop()
            maze[x][y] = "+"
            
            """This instead of below"""
            if (x,y) not in visited:
                visited.append((x,y))

            #visited.append((x,y))
        elif stack != [] and not hasAdj:
            maze[x][y] = "-"
            x,y = visited.pop()
        else:
            break

        if (x,y) == goal:
            success = True
            break
        hasAdj = False
        if maze[x][y+1] == " " or maze[x][y+1] == ".":
            stack.append((x,y+1))
            hasAdj = True
        if maze[x+1][y] == " " or maze[x+1][y] == ".":
            stack.append((x+1,y))
            hasAdj = True
        if maze[x][y-1] == " " or maze[x][y-1] == ".":
            stack.append((x,y-1))
            hasAdj = True
        if maze[x-1][y] == " " or maze[x-1][y] == ".":
            stack.append((x-1,y))
            hasAdj = True
    
        printMaze(maze)
        print("stack: ",stack)
        print("vistied: ",visited)

        

def breadthFirstSearch(maze):
    queue = []
    start = getStartPos(maze)
    print(start)
    x,y = start
    queue.append((x,y))
    success = False
    goal = getGoalPos(maze)

    while(not success):
        """yah = input("continue?")"""
        if queue != []:
            x,y = queue.pop(0)
        else:
            break
        
        if (x,y) == goal:
            success = True
            break
        
        if maze[x-1][y] == " " or maze[x-1][y] == ".":
            maze[x-1][y] = "v"
            queue.append((x-1,y))
            printMaze(maze)
        if maze[x][y-1] == " " or maze[x][y-1] == ".":
            maze[x][y-1] = ">"
            queue.append((x,y-1))
            printMaze(maze)
        if maze[x+1][y] == " " or maze[x+1][y] == ".":
            maze[x+1][y] = "^"
            queue.append((x+1,y))
            printMaze(maze)
        if maze[x][y+1] == " " or maze[x][y+1] == ".":
            maze[x][y+1] = "<"
            queue.append((x,y+1))
            printMaze(maze)
        
    print(returnPath(maze,start,goal))


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

    return 0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--method", help="method")
    parser.add_argument("maze", help="maze.txt")
    
    args = parser.parse_args()
    fileName = args.maze
    if path.exists(fileName):

        theMaze = mazeToArray(fileName)
       
        if args.method == "depth":
            #depthFirstSearch(theMaze)
            betterDepthFirst(theMaze)

        elif args.method == "breadth":
            breadthFirstSearch(theMaze)

        elif args.method == "greedy":
            greedSearch(theMaze)
            
        elif args.method == "astar":
            print("astar")
        else:
            print("Invalid operation")
            exit()
    else:
        print("Invalid file name")


if __name__ == "__main__":
    main()