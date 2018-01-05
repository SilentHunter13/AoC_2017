#!/usr/bin/env python3

import collections

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PATH_CHARACTERS = '|-+' + LETTERS

def empty_pixel():
    return ' '

class MazeRunner:

    def __init__(self, maze):
        self.maze = maze

        self.path_string = ''
        self.is_end = False
        self.x = 0
        self.y = 0
        self.steps = 0

        self.find_entry()

        #Startrichtung
        self.dx = 0
        self.dy = 1

    def find_entry(self):
        #Einstieg suchen
        while self.maze[(self.x, self.y)] != '|':
            self.x += 1

    def go_step(self):

        if self.maze[(self.x, self.y)] in PATH_CHARACTERS:
            self.steps += 1

            #neue Richtung bestimmen
            if self.maze[(self.x, self.y)] == '+':
                #nach links drehen
                self.dx, self.dy = self.dy, -self.dx

                new_x = self.x + self.dx
                new_y = self.y + self.dy
                if self.maze[(new_x, new_y)] not in PATH_CHARACTERS:
                    #nach rechts drehen
                    self.dx = self.dx * -1
                    self.dy = self.dy * -1

            #in die Richtung gehen
            self.x = self.x + self.dx
            self.y = self.y + self.dy

            #Pfad speichern
            if self.maze[(self.x, self.y)] in LETTERS:
                self.path_string += self.maze[(self.x, self.y)]
        else:
            self.is_end = True

    def run(self):

        while not self.is_end:
            self.go_step()

def day19():

    maze = collections.defaultdict(empty_pixel)

    with open('./Input/Day19.txt', 'r') as file:

        for (y, line) in enumerate(file.readlines()):
            for (x, str_pixel) in enumerate(line):
                maze[(x, y)] = str_pixel

        runner = MazeRunner(maze)

        runner.run()

    return (runner.path_string, runner.steps)

print(day19())
