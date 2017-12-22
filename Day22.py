#!/usr/bin/env python3

import numpy as np

GRID_SIZE = 1001

def set_index(matrix, point, value):

    matrix[(GRID_SIZE // 2) - point[1,0], (GRID_SIZE // 2) + point[0,0]] = value

def get_index(matrix, point):

    return matrix[(GRID_SIZE // 2) - point[1,0], (GRID_SIZE // 2) + point[0,0]]

class Carrier:

    def __init__(self):
        self.direction = np.array([(0),(1)], dtype = int).reshape(2,1)

        self.position = np.array([(0),(0)], dtype = int).reshape(2,1)
        self.infects = 0

    def calc_direction(self, infection):

        if infection == 1:
            #rechts
            turn = np.array([[0, 1], [-1, 0]])
        else:
            #links
            turn = np.array([[0, -1], [1, 0]])

        self.direction = np.dot(turn, self.direction)

    def infect(self, infection):

        if infection == 1:
            infection = 0
        else:
            infection = 1
            self.infects += 1

        return infection

    def burst(self, grid):

        infection = get_index(grid,self.position)
        #print(self.position)
        #print(infection)

        self.calc_direction(infection)
        #print(self.direction)

        set_index(grid, self.position, self.infect(infection))

        self.position = self.position + self.direction
        #print(self.position)

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
    for i in range(10000):
        #print(grid[496:505,496:505])
        carrier.burst(grid)

    return carrier.infects

print(day22())
