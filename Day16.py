#!/usr/bin/env python3


def day16():

    dance_line = list([x for x in 'abcdefghijklmnop'])

    with open('./Input/Day16.txt', 'r') as file:

        for line in file.readlines():
            moves = line.split(',')
            
            for move in moves:
                if move[0] == 's':
                    dance_line = dance_line[
                elif move[0] == 'x':
                
                elif move[0] == 'p':
            

print(day16())
