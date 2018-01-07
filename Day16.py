#!/usr/bin/env python3

import cProfile

SPIN = 0
EXCHANGE = 1
PARTNER = 2

LINE_WIDTH = 5

def bits(num):

    while num:
        yield bool(num & 0x01)
        num = num >> 1

class Dancer:

    def __init__(self, filename):
        self.sx_lookup = list(range(LINE_WIDTH))
        #self.p_lookup = list(range(LINE_WIDTH))

        self.char_line = list([x for x in 'abcdefghijklmnop'])

        with open(filename, 'r') as file:

            for line in file.readlines():
                self.read_moves(line)

    def read_moves(self, line):

        for str_move in line.split(','):
            str_move = str_move.strip()
            if str_move[0] == 's':
                move = {'type': SPIN, 'value1': int(str_move[1:])}
                spin_count = int(str_move[1:])
                if spin_count > 0:
                    self.sx_lookup = self.sx_lookup[-spin_count:] + self.sx_lookup[:LINE_WIDTH - spin_count]
            elif str_move[0] == 'x':
                move = {'type': EXCHANGE, 'value1': int(str_move[1:].split('/')[0]), 'value2': int(str_move[1:].split('/')[1])}
                pos1 = int(str_move[1:].split('/')[0])
                pos2 = int(str_move[1:].split('/')[1])
                self.sx_lookup[pos1], self.sx_lookup[pos2] = self.sx_lookup[pos2], self.sx_lookup[pos1]
            elif str_move[0] == 'p':
                move = {'type': PARTNER, 'value1': ord(str_move[1:].split('/')[0]) - 0x61, 'value2': ord(str_move[1:].split('/')[1]) - 0x61}


#def dance(dance_line, moves):
#    new_dance_line = dance_line[:]
#    for move in moves:
#        if move['type'] == SPIN:
#            if move['value1'] > 0:
#                new_dance_line = new_dance_line[-move['value1']:] + new_dance_line[:LINE_WIDTH - move['value1']]
#        elif move['type'] == EXCHANGE:
#            new_dance_line[move['value1']], new_dance_line[move['value2']] = new_dance_line[move['value2']], new_dance_line[move['value1']]
#        elif move['type'] == PARTNER:
#            index1 = new_dance_line.index(move['value1'])
#            index2 = new_dance_line.index(move['value2'])
#            new_dance_line[index1], new_dance_line[index2] = new_dance_line[index2], new_dance_line[index1]
#
#    return new_dance_line

    def dance(self, dance_count):
        sx_template = self.sx_lookup.copy()
        sx_line = list(range(LINE_WIDTH))
        for bit in bits(dance_count):
            #print(template_line)
            if bit:
                sx_line = dance_on(sx_line, sx_template)

            #neues sx Template berechnen
            sx_template = dance_on(sx_template, sx_template)
            print(sx_template)

        return sx_line

def dance_on(dance_line, template):

    new_dance_line = dance_line.copy()
    for index, element in enumerate(dance_line):
        new_dance_line[index] = dance_line[template[index]]

    return new_dance_line

def day16(dance_count):

    dancer = Dancer('./Input/Day16_t1.txt')


        #template_line = dance(dance_line, moves)

#        for _ in range(dance_count):
#            dance_line = dance(dance_line, moves)
#            print(dance_line)
#    return ''.join([char_line[c] for c in dance_line])
    return dancer.dance(dance_count)


print(day16(3))
#cProfile.run('day16(2)')
#print(day16(2))
#print(day16(3))
