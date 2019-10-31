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

    

    return 0


def depthFirstSearch(maze):

    """FINISH ADDING THE SOLUTION COST """
    solutionCost = 0
    activePath = []
    success = False
    while(not success):
        yah = input("continue?")

        """MAKE THIS INTO A SEPERATE METHOD, CURRENT POSITION"""
        for i in range(len(maze)):
            print()
            for x in range(len(maze[i])):
                if maze[i][x] == "P":
                    start = (i,x)
                print(maze[i][x],end="")
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
        



        for i in range(len(maze)):
            print()
            for x in range(len(maze[i])):
                print(maze[i][x],end="")

        """print(activePath)"""
        
    return 0

def breadthFirstSearch(maze):

    previousStates = []
    frontierStates = []
    success = False
    while(not success):
        yah = input("continue?")

        """GETS START POSITION"""
        for i in range(len(maze)):
            print()
            for x in range(len(maze[i])):
                if maze[i][x] == "P":
                    start = (i,x)
                print(maze[i][x],end="")
        x,y = start

    return 0

def greedSearch(maze):

    success = False
    while(not success):
        yah = input("continue?")
        for i in range(len(maze)):
            print()
            for x in range(len(maze[i])):
                if maze[i][x] == "P":
                    start = (i,x)
                elif maze[i][x] == ".":
                    goal = (i,x)
                print(maze[i][x],end="")
        x,y = start
        goalx,goaly = goal

        manhatDist = abs(x-goalx) + abs(y-goaly)


        """UP,LEFT,DOWN,RIGHT"""
        

    return 0

def aStarSearch(maze):

    success = False
    while(not success):

        for i in range(len(maze)):
            print()
            for x in range(len(maze[i])):
                if maze[i][x] == "P":
                    start = (i,x)
                elif maze[i][x] == ".":
                    goal = (i,x)
                print(maze[i][x],end="")
        x,y = start
        goalx,goaly = goal

        manhatDist = abs(x-goalx) + abs(y-goaly)

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