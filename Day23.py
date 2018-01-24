#! /usr/bin/env python

import re
import collections
import math

class Cpu:

    def __init__(self, instructions, debug):

        self.pc = 0
        self.mul_count = 0
        self.instructions = instructions
        self.registers = collections.defaultdict(int)
        self.registers['a'] = debug


    def execute(self):

        inst = self.instructions[self.pc]

        #Operand 2 decodieren
        if isinstance(inst['op1'], str):
            value1 = self.registers[inst['op1']]
        else:
            value1 = inst['op1']

        #Operand 2 decodieren
        if isinstance(inst['op2'], str):
            value2 = self.registers[inst['op2']]
        else:
            value2 = inst['op2']

        incpc = True

        if inst['code'] == 'set':
            self.registers[inst['op1']] = value2
        elif inst['code'] == 'sub':
            self.registers[inst['op1']] = self.registers[inst['op1']] - value2
        elif inst['code'] == 'mul':
            self.registers[inst['op1']] = self.registers[inst['op1']] * value2
            self.mul_count += 1
        elif inst['code'] == 'jnz':
            if value1 != 0:
                self.pc = self.pc + value2
                incpc = False

        if incpc:
            self.pc += 1

    def run(self):
        while self.pc < len(self.instructions):
            self.execute()

        return self.mul_count


def read_inst(line):

    parts = line.split()

    inst = dict()
    inst['code'] = parts[0]

    if re.match('[a-z]+', parts[1]):
        inst['op1'] = parts[1]
    else:
        inst['op1'] = int(parts[1])

    if re.match('[a-z]+', parts[2]):
        inst['op2'] = parts[2]
    else:
        inst['op2'] = int(parts[2])

    return inst

def day23():

    instructions = list()

    with open('./Input/Day23.txt', 'r') as file:

        for line in file.readlines():
            instructions.append(read_inst(line))

    cpu = Cpu(instructions, 0)

    return cpu.run()

def day23_opt():
    h = 0
    for i in range(108400, 125402, 17):
        f = 2
        divisible = False
        while f < math.sqrt(i):
            if (i % f) == 0:
                divisible = True
                break
            f += 1

        if divisible:
            h += 1

    return h

print(day23(), day23_opt())
