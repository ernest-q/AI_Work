

"""
Originally Found in http://aima.cs.berkeley.edu/python/

Markov Decision Processes 

First we define an MDP, and the special case of a GridMDP, in which
states are laid out in a 2-dimensional grid.  We also represent a policy
as a dictionary of {state:action} pairs, and a Utility function as a
dictionary of {state:number} pairs.  We then define the value_iteration
and policy_iteration algorithms."""

from utils2 import *

import argparse
from os import path

class MDP:
    """A Markov Decision Process, defined by an initial state, transition model,
    and reward function. We also keep track of a gamma value, for use by
    algorithms. The transition model is represented somewhat differently from
    the text.  Instead of T(s, a, s') being  probability number for each
    state/action/state triplet, we instead have T(s, a) return a list of (p, s')
    pairs.  We also keep track of the possible states, terminal states, and
    actions for each state. """

    def __init__(self, init, actlist, terminals, gamma=.9):
        update(self, init=init, actlist=actlist, terminals=terminals,
               gamma=gamma, states=set(), reward={})

    def R(self, state):
        "Return a numeric reward for this state."
        return self.reward[state]

    def T(state, action):
        """Transition model.  From a state and an action, return a list
        of (result-state, probability) pairs."""
        abstract

    def actions(self, state):
        """Set of actions that can be performed in this state.  By default, a
        fixed list of actions, except for terminal states. Override this
        method if you need to specialize by state."""
        if state in self.terminals:
            return [None]
        else:
            return self.actlist

class GridMDP(MDP):
    """A two-dimensional grid MDP, as in [Figure 17.1].  All you have to do is
    specify the grid as a list of lists of rewards; use None for an obstacle
    (unreachable state).  Also, you should specify the terminal states.
    An action is an (x, y) unit vector; e.g. (1, 0) means move east."""
    def __init__(self, grid, terminals, init=(0, 0), gamma=.9):
        grid.reverse() ## because we want row 0 on bottom, not on top
        MDP.__init__(self, init, actlist=orientations,
                     terminals=terminals, gamma=gamma)
        update(self, grid=grid, rows=len(grid), cols=len(grid[0]))
        for x in range(self.cols):
            for y in range(self.rows):
                self.reward[x, y] = grid[y][x]
                if grid[y][x] is not None:
                    self.states.add((x, y))

    def T(self, state, action):
        if action == None:
            return [(0.0, state)]
        else:
            return [(0.8, self.go(state, action)),
                    (0.1, self.go(state, turn_right(action))),
                    (0.1, self.go(state, turn_left(action)))]

    def go(self, state, direction):
        "Return the state that results from going in this direction."
        state1 = vector_add(state, direction)
        return if_(state1 in self.states, state1, state)

    def to_grid(self, mapping):
        """Convert a mapping from (x, y) to v into a [[..., v, ...]] grid."""
        return list(reversed([[mapping.get((x,y), None)
                               for x in range(self.cols)]
                              for y in range(self.rows)]))

    def to_arrows(self, policy):
        chars = {(1, 0):'>', (0, 1):'^', (-1, 0):'<', (0, -1):'v', None: '.'}
        return self.to_grid(dict([(s, chars[a]) for (s, a) in policy.items()]))


Fig= GridMDP([[-0.04, -0.04, -0.04, +1],
                     [-0.04, None,  -0.04, -1],
                     [-0.04, -0.04, -0.04, -0.04]],
                    terminals=[(3, 2), (3, 1)])

"""
Converts the maze file to the a format that is usable by 
the GridMDP class.
"""
def mazeToArray(mazeFile):

    file = open("{}".format(mazeFile),"r")
    contents = file.read()

    splitMaze = contents.split("\n")
    mazeArray = []

    for i in range(len(splitMaze)):
        innerMaze = []
        for x in range(len(splitMaze[i])):
            innerMaze.append(splitMaze[i][x])
        mazeArray.append(innerMaze)
    
    return mazeArray

def arrayToGrid(arrayMaze):
    valueGrid = []
    for z in range(len(arrayMaze)-1):
        valueGrid.append([])
    for y in range(1,len(valueGrid)):
        for x in range(1,len(arrayMaze[y])-1):
            if arrayMaze[y][x] == " ":
                valueGrid[y].append(-.04)
            elif arrayMaze[y][x] == "P":
                valueGrid[y].append(1)
            elif arrayMaze[y][x] == "N":
                valueGrid[y].append(-1)
            elif arrayMaze[y][x] == "%":
                valueGrid[y].append(None)

    return valueGrid

def findTerminal(mazeArray):
    terminals = []
    for y in range(len(mazeArray)):
        for x in range(len(mazeArray[y])):
            if mazeArray[y][x] == "P" or mazeArray[y][x] == "N":
                terminals.append((y+1,x))
    return terminals


def value_iteration(mdp, epsilon=0.001):
    "Solving an MDP by value iteration. [Fig. 17.4]"
    U1 = dict([(s, 0) for s in mdp.states])
    R, T, gamma = mdp.R, mdp.T, mdp.gamma
    while True:
        U = U1.copy()
        delta = 0
        for s in mdp.states:
            U1[s] = R(s) + gamma * max([sum([p * U[s1] for (p, s1) in T(s, a)])
                                        for a in mdp.actions(s)])
            delta = max(delta, abs(U1[s] - U[s]))
        if delta < epsilon * (1 - gamma) / gamma:
             return U

def best_policy(mdp, U):
    """Given an MDP and a utility function U, determine the best policy,
    as a mapping from state to action. (Equation 17.4)"""
    pi = {}
    for s in mdp.states:
        pi[s] = argmax(mdp.actions(s), lambda a:expected_utility(a, s, U, mdp))
    return pi

def expected_utility(a, s, U, mdp):
    "The expected utility of doing a in state s, according to the MDP and U."
    return sum([p * U[s1] for (p, s1) in mdp.T(s, a)])


def main():
    """#demo
    m = Fig
    print(m)
    pi = best_policy(m, value_iteration(m, .01))
    print(pi)
    print(m.to_arrows(pi))
    print(value_iteration(m, .01))"""

    parser = argparse.ArgumentParser()
    parser.add_argument("maze",help="maze.txt")
    args = parser.parse_args()
    mazeFile = args.maze
    if path.exists(mazeFile):

        convertedMaze = mazeToArray(mazeFile)
        for x in range(len(convertedMaze)):
            print()
            for y in range(len(convertedMaze[x])):
                print(convertedMaze[x][y],end="")

        terms = findTerminal(convertedMaze)

        grid = arrayToGrid(convertedMaze)
        for x in range(len(grid)):
            print()
            for y in range(len(grid[x])):
                print(grid[x][y],end="")
        
        newMDPGrid = []
        newMDPGrid.append(grid)
        newMDPGrid.append(terms)

    """grid = grid[::-1]
    for x in range(len(grid)):
            print()
            for y in range(len(grid[x])):
                print(grid[x][y],end="")"""

    
    print(findTerminal(convertedMaze))
    m = GridMDP(newMDPGrid,findTerminal(convertedMaze))
    print(m)
    pi = best_policy(m, value_iteration(m, .01))
    print(pi)
    print(m.to_arrows(pi))
    print(value_iteration(m, .01))

if __name__ == "__main__":
    main()