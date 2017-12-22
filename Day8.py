#!/usr/bin/env python3

import re

def decode_inst(line):

    parts = line.split()

    inst = dict()
    inst['register'] = parts[0]
    inst['op'] = parts[1]
    inst['value'] = int(parts[2])
    inst['condition'] = dict()
    inst['condition']['register'] = parts[4]
    inst['condition']['comparison'] = parts[5]
    inst['condition']['value'] = int(parts[6])

    return inst

def check_condition(registers, condition):

    result = False

    if condition['comparison'] == '>':
        result = registers.get(condition['register'], 0) > condition['value']
    elif condition['comparison'] == '>=':
        result = registers.get(condition['register'], 0) >= condition['value']
    elif condition['comparison'] == '<':
        result = registers.get(condition['register'], 0) < condition['value']
    elif condition['comparison'] == '<=':
        result = registers.get(condition['register'], 0) <= condition['value']
    elif condition['comparison'] == '!=':
        result = registers.get(condition['register'], 0) != condition['value']
    elif condition['comparison'] == '==':
        result = registers.get(condition['register'], 0) == condition['value']

    return result

def execute(registers, inst):

    if inst['op'] == 'inc':
        registers[inst['register']] = registers.get(inst['register'], 0) + inst['value']
    elif inst['op'] == 'dec':
        registers[inst['register']] = registers.get(inst['register'], 0) - inst['value']

def day8():

    registers = dict()

    high = 0

    with open('./Input/Day8.txt', 'r') as file:

        for line in file.readlines():

            inst = decode_inst(line)

            if check_condition(registers, inst['condition']):
                execute(registers, inst)

                high = max(high, registers[max(registers.keys(), key=lambda x:registers[x])])

    return (registers[max(registers.keys(), key=lambda x:registers[x])], high)

print(day8())
