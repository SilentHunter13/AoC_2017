#! usr/bin/env python3

import numpy as np

MATRIX_SIZE = 10000

def set_index(matrix, point, value):

    matrix[point[0,0] + (MATRIX_SIZE // 2), point[1,0] + (MATRIX_SIZE // 2)] = value

def get_index(matrix, point):

    return matrix[point[0,0] + (MATRIX_SIZE // 2), point[1,0] + (MATRIX_SIZE // 2)]

def get_direction(matrix, point, direction):

    #Drehmatrix
    turn = np.array([[0, -1], [1, 0]])

    #Richtung nach links drehen
    new_direction = np.dot(turn, direction)

    #Position zur linken ausrechnen
    left_neighbour = point + new_direction

    #prüfen, ob dort frei
    if get_index(matrix, left_neighbour) == 0:
        direction = new_direction

    return direction

def plus_one(old_value, matrix, point):

    return old_value + 1

def Day3(puzzle_input, get_new_value):

    value = 0
    point = np.zeros([2,1], dtype = int)
    direction = np.array([(1),(0)], dtype = int).reshape(2,1)
    matrix = np.zeros((MATRIX_SIZE, MATRIX_SIZE), dtype = int)

    while value < puzzle_input:
        #Wert erhöhen
        value = get_new_value(value, matrix, point)

        #Wert schreiben
        set_index(matrix, point, value)

        #neue Richtung berechnen
        direction = get_direction(matrix, point, direction)

        #in die Richtung weitergehen
        point = point + direction

    #letzen Schritt zurücknehmen
    point = point - direction
    return abs(point[0,0]) + abs(point[1,0])

print(Day3(361527, plus_one))
