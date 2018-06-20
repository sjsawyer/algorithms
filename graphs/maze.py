#! /usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque
from copy import deepcopy


class Maze:

    # Valid actions
    valid_actions = dict(left='←', up='↑', right='→', down='↓',)

    # Block types
    blocks = dict(invalid='#',
                  valid='.',
                  start='s',
                  end='e',
                  path='*',)

    def __init__(self, mazefile):
        self.mazefile = mazefile
        self.grid = None
        self.start = None
        self.end = None
        self.graph = dict()
        self.path = None
        self.actions_taken = None
        # load grid, start, end, graph
        self._load()


    def _get_action(self, parent, child):
        '''
        Get the action taken.
        Note in this implementation (0,0) is the upper left corner of the maze,
        the first axis is vertical, and the second axis is horizontal.

        '''
        if child[0] < parent[0]:
            return self.valid_actions['up']
        if child[0] > parent[0]:
            return self.valid_actions['down']
        if child[1] < parent[1]:
            return self.valid_actions['left']
        if child[1] > parent[1]:
            return self.valid_actions['right']

    def _isvalid(self, coord):
        ''' utility method to see if a coordinate is a block square '''
        return self.grid[coord[0]][coord[1]] != self.blocks['invalid']

    def _makeedge(self, coord1, coord2):
        ''' utility method to add an edge to our graph '''
        self.graph[coord1].add(coord2)
        self.graph[coord2].add(coord1)

    def _load(self):
        '''
        Convert a maze file, containing a maze represented by invalid "#"
        squares, valid "." squares, a start "s", and an end "e", into a graph
        represented by an adjacency list, whose nodes are coordinate (i,j)
        pairs.

        Sets the grid and graph attributes, as well as the start and end node
        attributes.

        '''
        with open(self.mazefile, 'rt') as f:
            rows = map(lambda x: x.strip(), f.readlines())
        # set grid attribute
        self.grid = map(list, rows)
        # connect by looking down and to the right
        # represent each node as a coordinate, and only store valid squares
        # in the graph (e.g. no # squares)
        nrows = len(self.grid)
        ncols = len(self.grid[0])
        for i in range(nrows):
            for j in range(ncols):
                if self.grid[i][j] == 's':
                    self.start = (i, j)
                if self.grid[i][j] == 'e':
                    self.end = (i, j)
                if self._isvalid((i, j)):
                    self.graph[(i, j)] = set()
        # Add edges to our graph
        for i in range(nrows):
            for j in range(ncols):
                if self._isvalid((i, j)):
                    if i < nrows-1:
                        if self._isvalid((i+1, j)):
                            self._makeedge((i, j), (i+1, j))
                    if j < ncols-1:
                        if self._isvalid((i, j+1)):
                            self._makeedge((i, j), (i, j+1))

    def solve(self):
        '''
        Find a path in a BFS manner using the graph, start node and end node
        '''
        # keep track of vertices we've seen so we don't revisit them
        seen = set()
        # FIFO queue to search vertices in a BFS manner
        tovisit = deque()
        # Keep track of where we've come from to reconstruct the path,
        # and the action taken from node to node
        meta = {}
        # Initialize
        seen.add(self.start)
        tovisit.append(self.start)
        # While we still have nodes to visit, commence BFS
        while tovisit:
            current = tovisit.popleft()
            for neighbour in self.graph[current]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    tovisit.append(neighbour)
                    # keep track of the path
                    action = self._get_action(current, neighbour)
                    meta[neighbour] = (current, action)
                    if neighbour == self.end:
                        # we can stop here
                        break
        # We have found the path
        actions = []
        path = []
        node = self.end
        while node != self.start:
            parent, action = meta[node]
            actions.append(action)
            path.append(node)
            node = parent
        path.append(self.start)
        actions.reverse()
        path.reverse()
        # Set our path and actions attributes
        self.path = path
        self.actions_taken = ' '.join(actions)

    def print_solution(self):
        '''
        Print the maze with the solution indicated by '*'s
        '''
        solved_grid = deepcopy(self.grid)
        # Sort the path by rows
        path = sorted(self.path, key=lambda x: x[1])
        # Group the path by rows
        rows = [set() for row in solved_grid]
        for coord in path:
            rows[coord[0]].add(coord[1])
        for i in range(len(solved_grid)):
            for j in range(len(solved_grid[0])):
                if j in rows[i]:
                    # This node is part of the soluton
                    solved_grid[i][j] = self.blocks['path']
        # print the solved grid
        solution_str = '\n'.join(''.join(block for block in row)
                                 for row in solved_grid)
        print "Solved Maze:\n\n{}\n".format(solution_str)
        print "Actions taken: {}".format(self.actions_taken)


def main():
    mazefile = "sample_graphs/maze.txt"
    maze = Maze(mazefile)
    maze.solve()
    maze.print_solution()


if __name__ == '__main__':
    main()
