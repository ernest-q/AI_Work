import argparse
import os.path
from os import path


def mazeToArray(fileSelect):

    file = open("{}".format(fileSelect),"r")
    contents = file.read()
    print(contents)
    print(type(contents))

    split = contents.split("\n")
    """print(split)"""
    for i in range(len(split)):
        print(split[i])

    mazeArray = []
    for i in range(len(split)):
        print()
        innerMaze = []
        for x in range(len(split[i])):
            print(split[i][x],end="")
            innerMaze.append(split[i][x])
        mazeArray.append(innerMaze)
    
    depthFirstSearch(mazeArray)

    return mazeArray

def printMaze(maze):
    for i in range(len(maze)):
            print()
            for x in range(len(maze[i])):
                print(maze[i][x],end="")

def getStartPos(maze):
    for i in range(len(maze)):
            print()
            for x in range(len(maze[i])):
                if maze[i][x] == "P":
                    start = (i,x)
    
    return start

def getGoalPos(maze):
    for i in range(len(maze)):
            print()
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
        yah = input("continue?")

        """GETS THE START POSITION"""
        start = getStartPos(maze)
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
        

def breadthFirstSearch(maze):

    previousStates = []
    frontierStates = []
    success = False
    while(not success):
        yah = input("continue?")

        """GETS START POSITION"""
        start = getStartPos(maze)
        x,y = start

    return 0

def calcManDistance((startX,startY),(goalX,goalY)):
    manhatDist = abs(startX - goalX) + abs(startY - goalY)
    return manhatDist

def greedSearch(maze):

    success = False
    while(not success):
        yah = input("continue?")
        start = getStartPos(maze)
        goal = getGoalPos(maze)
        x,y = start
        goalx,goaly = goal

        heuristic = calcManDistance(start,goal)

        """UP,LEFT,DOWN,RIGHT"""
        

    return 0

def aStarSearch(maze):

    success = False
    while(not success):

        start = getStartPos(maze)
        goal = getGoalPos(maze)
        x,y = start
        goalx,goaly = goal

        heuristic = calcManDistance(start,goal)

        """UP,LEFT,DOWN,RIGHT"""
        
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--method", help="method")
    parser.add_argument("maze", help="maze.txt")
    
    args = parser.parse_args()
    """print(args.method)
    print(args.maze)"""
    fileName = args.maze
    
    if path.exists(fileName):

        theMaze = mazeToArray(fileName)
        print(theMaze)

        if args.method == "depth":
            depthFirstSearch(theMaze)
            print("dep")
        elif args.method == "breadth":
            print("bred")
        elif args.method == "greedy":
            print("greed")
        elif args.method == "astar":
            print("astar")
        else:
            print("Invalid operation")
    else:
        print("Invalid file name")


if __name__ == "__main__":
    main()