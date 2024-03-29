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

def printMaze(maze):
    for i in range(len(maze)):
            print()
            for x in range(len(maze[i])):
                print(maze[i][x],end="")

def mazeToArray(fileSelect):

    file = open("{}".format(fileSelect),"r")
    contents = file.read()

    splitMaze = contents.split("\n")
    mazeArray = []

    for i in range(len(splitMaze)):
        innerMaze = []
        for x in range(len(splitMaze[i])):
            innerMaze.append(splitMaze[i][x])
        mazeArray.append(innerMaze)
    
    return mazeArray


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


def calcManDistance(startX,startY,goalX,goalY):

    manhatDist = abs(startX - goalX) + abs(startY - goalY)
    return manhatDist


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
        up,left,down,right = checkAdj(maze,x,y,visited)

        if (x,y) not in visited:
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
        
    printMazePathCost(maze,root,visited)


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

        up,left,down,right = checkAdj(maze,x,y,visited)
        if (x,y) not in visited:
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
    
    printMazePathCost(maze,root,visited)


def bettergreedSearch(maze):

    start = getStartPos(maze)
    goal = getGoalPos(maze)
    goalx, goaly = goal
    x,y = start
    root = Node((x,y))
    pq = PriorityQueue()
    pq.put((1,1,id(root),(root)))

    visited = []

    success = False
    while not success:
        z = pq.get()
        h = z[0]
        x,y = z[3].getCargo()
        root = z[3]

        if h == 0:
            break
        up,left,down,right = checkAdj(maze,x,y,visited)

        if (x,y) not in visited:
            visited.append((x,y))

        if up:
            newNode1 = Node((x-1,y),root)
            heuristic = calcManDistance(x-1,y,goalx,goaly)
            pq.put((heuristic,1,id(newNode1),(newNode1)))
        if left:
            newNode2 = Node((x,y-1),root)
            heuristic = calcManDistance(x,y-1,goalx,goaly)
            pq.put((heuristic,2,id(newNode2),(newNode2)))
        if down:
            newNode3 = Node((x+1,y),root)
            heuristic = calcManDistance(x+1,y,goalx,goaly)
            pq.put((heuristic,3,id(newNode3),(newNode3)))
        if right:
            newNode4 = Node((x,y+1),root)
            heuristic = calcManDistance(x,y+1,goalx,goaly)
            pq.put((heuristic,4,id(newNode4),(newNode4)))

    printMazePathCost(maze,root,visited)


def betteraStarSearch(maze):

    start = getStartPos(maze)
    goal = getGoalPos(maze)
    goalx, goaly = goal
    x,y = start
    root = Node((x,y))
    pq = PriorityQueue()
    pq.put((1,0,id(root),(root)))

    visited = []

    success = False
    while not success:
        z = pq.get()
        h = z[0]
        sp = z[1]
        x,y = z[3].getCargo()
        root = z[3]

        if (x,y) == (goalx,goaly):
            break
        up,left,down,right = checkAdj(maze,x,y,visited)

        if (x,y) not in visited:
            visited.append((x,y))

        stepCost = (sp+1)
        if up:
            newNode1 = Node((x-1,y),root)
            heuristic = calcManDistance(x-1,y,goalx,goaly) + stepCost
            pq.put((heuristic,stepCost,id(newNode1),(newNode1)))
        if left:
            newNode2 = Node((x,y-1),root)
            heuristic = calcManDistance(x,y-1,goalx,goaly) + stepCost
            pq.put((heuristic,stepCost,id(newNode2),(newNode2)))
        if down:
            newNode3 = Node((x+1,y),root)
            heuristic = calcManDistance(x+1,y,goalx,goaly) + stepCost
            pq.put((heuristic,stepCost,id(newNode3),(newNode3)))
        if right:
            newNode4 = Node((x,y+1),root)
            heuristic = calcManDistance(x,y+1,goalx,goaly) + stepCost
            pq.put((heuristic,stepCost,id(newNode4),(newNode4)))

    printMazePathCost(maze,root,visited)    


def printMazePathCost(maze,node,visited):

    path = []
    while node.getParent() != None:
        x,y = node.getCargo()
        path.insert(0,(x,y))
        maze[x][y] = "0"
        node = node.parent
    printMaze(maze)
    print("\nSOLUTION: ",path) 
    print("\nSOLUTION COST: ",len(path))
    print("\n# OF EXPANDED NODES:{} \n".format(len(visited)))


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
            #greedSearch(theMaze)
            bettergreedSearch(theMaze)
            
        elif args.method == "astar":
            #aStarSearch(theMaze)
            betteraStarSearch(theMaze)
        else:
            print("Invalid operation")
            exit()
    else:
        print("Invalid file name")


if __name__ == "__main__":
    main()