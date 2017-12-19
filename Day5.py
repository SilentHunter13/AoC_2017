#!/usr/bin/env python3

import numpy as np

MATRIX_SIZE = 1052

def inc_offset(index):

    return index + 1

def Day5(calc_offset):

    array = np.zeros((MATRIX_SIZE), dtype = int)

    with open('./Input/Day5.txt', 'r') as file:

        for (index, number) in enumerate(file.readlines()):

            array[index] = int(number)

    index = 0
    step = 0

    while index < len(array):

        newindex = index + array[index]
        array[index] = calc_offset(array[index])
        step += 1
        index = newindex

    return step

print(Day5(inc_offset))
