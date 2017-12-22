#!/usr/bin/env python3

import numpy as np

def decode_connection(join_mat, line):

    parts = line.split('<->')

    partners = parts[1].split(',')

    for partner in partners:

        join_mat[int(parts[0]), int(partner)] = True

def day12():

    join_mat = np.zeros((2000,2000), dtype = bool)

    with open('./Input/Day12.txt', 'r') as file:

        for line in file.readlines():
            decode_connection(join_mat, line)

    ready = False

    while not ready:

        old = np.array(join_mat[0,:])
        for index, row in enumerate(join_mat):
            if index in list(np.where(join_mat[0,:] == True)[0]):
                join_mat[0,:] = join_mat[0,:] | row

        if (old == join_mat[0,:]).all():
            ready = True


    return np.sum(join_mat[0,:])

print(day12())
