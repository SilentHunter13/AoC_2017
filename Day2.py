#!/usr/bin/env python3

import sys

def min_max_diff(line):
    min = sys.maxsize
    max = 0
    for str_number in line.split():

        number = int(str_number)
        if number > max:
          max = number
        if number < min:
          min = number
    return (max - min)

def Day2(line_value_get):

    checksum = 0

    with open('./Input/Day2.txt', 'r') as file:

        for line in file.readlines():

            checksum = checksum + line_value_get(line)

    return checksum

print(Day2(min_max_diff))
