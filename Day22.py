#!/usr/bin/env python3

import numpy as np
import time

GRID_SIZE = 1001
HALF_GRID_SIZE = GRID_SIZE // 2

def set_index(matrix, point, value):

    matrix[HALF_GRID_SIZE - point[1,0], HALF_GRID_SIZE + point[0,0]] = value

def get_index(matrix, point):

    return matrix[HALF_GRID_SIZE - point[1,0], HALF_GRID_SIZE + point[0,0]]

class Carrier:

    def __init__(self):

        self.direction = np.array([(0),(1)], dtype = int).reshape(2,1)

        self.position = np.array([(0),(0)], dtype = int).reshape(2,1)
        self.infects = 0

        # clean = 0, infected = 1, weakend = -1, flagged = 0.5
        self.action = {1:0.5, -1:1, 0:-1, 0.5:0}

        self.turn = dict()
        self.turn[1] = np.array([[0, 1], [-1, 0]])
        self.turn[0] = np.array([[0, -1], [1, 0]])
        self.turn[-1] = np.array([[1, 0], [0, 1]])
        self.turn[0.5] = np.array([[-1, 0], [0, -1]])

    def calc_direction(self, status):

        self.direction = np.dot(self.turn[status], self.direction)

    def infect(self, status):

        if status == -1:
            self.infects += 1

        return self.action[status]

    def burst(self, grid):

        infection = get_index(grid,self.position)

        self.calc_direction(infection)

        set_index(grid, self.position, self.infect(infection))

        self.position = self.position + self.direction

def decode_line(line):
    line = line.strip()
    line = line.replace('#', '1')
    line = line.replace('.','0')

    vector = np.array(list(line))
    vector.shape = (1,len(line))

    return vector

def day22():

    grid = np.zeros((GRID_SIZE, GRID_SIZE))

    with open('./Input/Day22.txt', 'r') as file:

        for (index, line) in enumerate(file.readlines()):

            input_length = len(line.strip())
            insert_index = 500 - (input_length // 2)
            grid[insert_index + index:insert_index + index + 1,insert_index:insert_index + input_length] = decode_line(line)

    carrier = Carrier()

    start =  time.clock()
    for i in range(10000000):
        carrier.burst(grid)

    stop =  time.clock()
    print(stop - start)

    return carrier.infects

print(day22())
