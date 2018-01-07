#!/usr/bin/env python3

import cProfile

SPIN = 0
EXCHANGE = 1
PARTNER = 2

LINE_WIDTH = 16

def bits(num):

    while num:
        yield bool(num & 0x01)
        num = num >> 1

class Dancer:

    def __init__(self, filename):
        self.sx_lookup = list(range(LINE_WIDTH))
        self.p_lookup = list(range(LINE_WIDTH))

        self.char_line = list([x for x in 'abcdefghijklmnop'])

        with open(filename, 'r') as file:

            for line in file.readlines():
                self.read_moves(line)

    def read_moves(self, line):

        for str_move in line.split(','):
            str_move = str_move.strip()
            if str_move[0] == 's':
                spin_count = int(str_move[1:])
                if spin_count > 0:
                    self.sx_lookup = self.sx_lookup[-spin_count:] + self.sx_lookup[:LINE_WIDTH - spin_count]
            elif str_move[0] == 'x':
                pos1 = int(str_move[1:].split('/')[0])
                pos2 = int(str_move[1:].split('/')[1])
                self.sx_lookup[pos1], self.sx_lookup[pos2] = self.sx_lookup[pos2], self.sx_lookup[pos1]
            elif str_move[0] == 'p':
                value1 = ord(str_move[1:].split('/')[0]) - ord('a')
                value2 = ord(str_move[1:].split('/')[1]) - ord('a')
                index1 = self.p_lookup.index(value1)
                index2 = self.p_lookup.index(value2)
                self.p_lookup[index1], self.p_lookup[index2] = self.p_lookup[index2], self.p_lookup[index1]

    def dance(self, dance_count):
        sx_template = self.sx_lookup.copy()
        p_template = self.p_lookup.copy()
        sx_line = list(range(LINE_WIDTH))
        p_line = list(range(LINE_WIDTH))
        for bit in bits(dance_count):
            if bit:
                sx_line = dance_sx(sx_line, sx_template)
                p_line = dance_p(p_line, p_template)

            #neue Templates berechnen
            sx_template = dance_sx(sx_template, sx_template)
            p_template = dance_p(p_template, p_template)

        return ''.join([self.char_line[c] for c in dance_p(sx_line, p_line)])

def dance_sx(dance_line, template):

    new_dance_line = dance_line.copy()
    for index, _ in enumerate(dance_line):
        new_dance_line[index] = dance_line[template[index]]

    return new_dance_line

def dance_p(dance_line, template):

    new_dance_line = dance_line.copy()
    for index, _ in enumerate(dance_line):
        new_dance_line[index] = template[dance_line[index]]

    return new_dance_line

def day16(dance_count):

    dancer = Dancer('./Input/Day16.txt')

    return dancer.dance(dance_count)


print(day16(1))
print(day16(1000000000))
#cProfile.run('day16(2)')
#print(day16(2))
#print(day16(3))
