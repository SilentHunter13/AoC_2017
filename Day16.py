#!/usr/bin/env python3

import cProfile
import array

SPIN = 0
EXCHANGE = 1
PARTNER = 2

LINE_COUNT = 16

def bits(num):

    while num:
        yield bool(num & 0x01)
        num = num >> 1

def read_moves(line):

    moves = list()
    for str_move in line.split(','):
        str_move.strip()
        if str_move[0] == 's':
            move = {'type': SPIN, 'value1': int(str_move[1:])}
        elif str_move[0] == 'x':
            move = {'type': EXCHANGE, 'value1': int(str_move[1:].split('/')[0]), 'value2': int(str_move[1:].split('/')[1])}
        elif str_move[0] == 'p':
            move = {'type': PARTNER, 'value1': ord(str_move[1:].split('/')[0]) - 0x61, 'value2': ord(str_move[1:].split('/')[1]) - 0x61}

        moves.append(move)

    return moves

def dance(dance_line, moves):
    new_dance_line = dance_line[:]
    for move in moves:
        if move['type'] == SPIN:
            if move['value1'] > 0:
                new_dance_line = new_dance_line[-move['value1']:] + new_dance_line[:LINE_COUNT - move['value1']]
        elif move['type'] == EXCHANGE:
            new_dance_line[move['value1']], new_dance_line[move['value2']] = new_dance_line[move['value2']], new_dance_line[move['value1']]
        elif move['type'] == PARTNER:
            index1 = new_dance_line.index(move['value1'])
            index2 = new_dance_line.index(move['value2'])
            new_dance_line[index1], new_dance_line[index2] = new_dance_line[index2], new_dance_line[index1]

    return new_dance_line

def dance_on(dance_line, template):

    new_dance_line = dance_line[:]
    for index, element in enumerate(dance_line):
        new_dance_line[index] = dance_line[template[index]]

    return new_dance_line

def day16(dance_count):

    char_line = list([x for x in 'abcdefghijklmnop'])
    dance_line = array.array('I', range(LINE_COUNT))

    with open('./Input/Day16.txt', 'r') as file:

        for line in file.readlines():
            moves = read_moves(line)

        template_line = dance(dance_line, moves)

        for bit in bits(dance_count):
            if bit:
                print(dance_line)
                dance_line = dance_on(dance_line, template_line)

            #neue Templates berechnen
            template_line = dance_on(template_line, template_line)

#        for _ in range(dance_count):
#            dance_line = dance(dance_line, moves)
    print(dance_line)
    return ''.join([char_line[c] for c in dance_line])


print(day16(1))
#cProfile.run('day16(2)')
#print(day16(1000000000))
