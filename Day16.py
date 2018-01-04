#!/usr/bin/env python3


def day16():

    dance_line = list([x for x in 'abcdefghijklmnop'])

    with open('./Input/Day16.txt', 'r') as file:

        for line in file.readlines():
            moves = line.split(',')

            for move in moves:
                if move[0] == 's':
                    count = int(move[1:])
                    if count > 0:
                        dance_line = dance_line[-count:] + dance_line[:len(dance_line) - count]
                elif move[0] == 'x':
                    positions = [int(x) for x in move[1:].split('/')]
                    dance_line[positions[0]], dance_line[positions[1]] = dance_line[positions[1]], dance_line[positions[0]]
                elif move[0] == 'p':
                    partners = move[1:].split('/')
                    index = [dance_line.index(x) for x in partners]
                    dance_line[index[0]], dance_line[index[1]] = dance_line[index[1]], dance_line[index[0]]

    return ''.join(dance_line)


print(day16())
