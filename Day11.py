#!/usr/bin/env python3

def go_direction(position, direction):

    delta = (0, 0)
    if direction == 'n':
        delta = (0, 2)
    elif direction == 'ne':
        delta = (2, 1)
    elif direction == 'se':
        delta = (2, -1)
    elif direction == 's':
        delta = (0, -2)
    elif direction == 'sw':
        delta = (-2, -1)
    elif direction == 'nw':
        delta = (-2, 1)

    return (position[0] + delta[0], position[1] + delta[1])

def calc_shortest_distance(position):

    #es ist nur die Lösung für einen Quadranten nötig
    #Lösung für Quadrant 1 (x und y positiv)
    position = (abs(position[0]), abs(position[1]))

    #x Wert kleiner gleich zweifacher y Wert
    if position[0] <= (position[1] * 2):
        steps = position[0] // 2
        steps += (position[1] - steps) // 2
    else:
        steps = position[1]
        steps += (position[0] - (steps * 2)) // 2

    return steps


def day11():

    position = (0, 0)
    max_steps = 0

    with open('./Input/Day11.txt', 'r') as file:

        for line in file.readlines():
            path = [x.strip() for x in line.split(',')]

            for direction in path:

                position = go_direction(position, direction)
                max_steps = max(max_steps, calc_shortest_distance(position))

    steps = calc_shortest_distance(position)

    return (steps, max_steps)

print(day11())
