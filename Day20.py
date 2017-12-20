#!/usr/bin/env python3

import re
import numpy as np
import itertools
import time

DIMENSIONS = 3

class Point:

    def __init__(self, line):

        self.collides = False
        self._position = np.zeros(DIMENSIONS)
        self._velocity = np.zeros(DIMENSIONS)
        self._acceleration = np.zeros(DIMENSIONS)

        result = re.match('p=<([-0-9]+),([-0-9]+),([-0-9]+)>, v=<([-0-9]+),([-0-9]+),([-0-9]+)>, a=<([-0-9]+),([-0-9]+),([-0-9]+)>', line)

        if result:
            self._position[0] = result.group(1)
            self._position[1] = result.group(2)
            self._position[2] = result.group(3)

            self._velocity[0] = result.group(4)
            self._velocity[1] = result.group(5)
            self._velocity[2] = result.group(6)

            self._acceleration[0] = result.group(7)
            self._acceleration[1] = result.group(8)
            self._acceleration[2] = result.group(9)

    def __repr__(self):

        repr = 'p={0}; v={1}; a={2}'.format(self._position, self._velocity, self._acceleration)

        return repr

    def step(self):

        self._velocity = self._velocity + self._acceleration

        self._position = self._position + self._velocity

    def get_distance(self):

        distance = abs(self._position[0])
        distance += abs(self._position[1])
        distance += abs(self._position[2])

        return distance

    def collide(self, other):

        if self is not other:
            if (self._position == other._position).all():
                self.collides = True
                other.collides = True

def remove_collisions(points):

    for point1, point2 in itertools.combinations(points, 2):
        point1.collide(point2)

    for point in points:
        if point.collides:
            points.remove(point)

def day20(remove, stay_target):

    points = list()

    with open('./Input/Day20.txt', 'r') as file:

        for line in file.readlines():

            points.append(Point(line))

    stay_counter = 0
    old_nearest = None
    old_len = 0

    while stay_counter < stay_target:
        for point in points:
            point.step()

        if remove:
            remove_collisions(points)

            if len(points) == old_len:
                stay_counter += 1
            else:
                stay_counter = 0

            old_len = len(points)

        else:
            nearest = min(points, key=lambda p: p.get_distance())

            if old_nearest == nearest:
                stay_counter += 1
            else:
                stay_counter = 0

                old_nearest = nearest

    if remove:
        return len(points)
    else:
        return points.index(nearest)

print(day20(False, 200))
print(day20(True, 10))
