#! /usr/bin/env python

import re
import collections

class Cpu:

    def __init__(self, instructions, sendqueue, receivequeue, cpu_id):

        self.pc = 0
        self.send_count = 0
        #self.rcv = False
        self.sendqueue = sendqueue
        self.receivequeue = receivequeue
        self.instructions = instructions
        self.registers = collections.defaultdict(int)
        self.registers['p'] = cpu_id
        self.cpu_id = cpu_id

    def _get_flex_value(self, op):
        if isinstance(op, str):
            value = self.registers[op]
        else:
            value = op

        return value

    def execute(self):

        inst = self.instructions[self.pc]

        #Operand 1 decodieren
        value1 = self._get_flex_value(inst['op1'])

        #Operand 2 decodieren
        if 'op2' in inst.keys():
            value2 = self._get_flex_value(inst['op2'])

        incpc = True
        waiting = False

        if inst['code'] == 'snd':
            self.send_count += 1
            self.sendqueue.append(value1)
        elif inst['code'] == 'set':
            self.registers[inst['op1']] = value2
        elif inst['code'] == 'add':
            self.registers[inst['op1']] = value1 + value2
        elif inst['code'] == 'mul':
            self.registers[inst['op1']] = value1 * value2
        elif inst['code'] == 'mod':
            self.registers[inst['op1']] = value1 % value2
        elif inst['code'] == 'rcv':
            try:
                self.registers[inst['op1']] = self.receivequeue.popleft()
            except IndexError:
                incpc = False
                waiting = True
        elif inst['code'] == 'jgz':
            if value1 > 0:
                self.pc = self.pc + value2
                incpc = False

        if incpc:
            self.pc += 1

        ret = 0
        if self.pc >= len(self.instructions):
            ret = 2
        elif waiting:
            ret = 1

        print(self.cpu_id, self.pc, waiting, self.registers)

        return (ret, self.send_count)

def run(instructions):

    cpu1_2_cpu2 = collections.deque()
    cpu2_2_cpu1 = collections.deque()

    cpu1 = Cpu(instructions, cpu1_2_cpu2, cpu2_2_cpu1, 0)
    cpu2 = Cpu(instructions, cpu2_2_cpu1, cpu1_2_cpu2, 1)

    ret1 = 0
    ret2 = 0
    count = 0
    while ((ret1 < 1) or (ret2 < 1)) and (count < 0):
        if ret1 < 2:
            (ret1, send_count1) = cpu1.execute()
        if ret2 < 2:
            (ret2, _) = cpu2.execute()

        count += 1

    return send_count1


def read_inst(line):

    parts = line.split()

    inst = dict()
    inst['code'] = parts[0]

    if re.match('[a-z]+', parts[1]):
        inst['op1'] = parts[1]
    else:
        inst['op1'] = int(parts[1])

    if len(parts) == 3:
        if re.match('[a-z]+', parts[2]):
            inst['op2'] = parts[2]
        else:
            inst['op2'] = int(parts[2])

    return inst

def day18():

    instructions = list()

    with open('./Input/Day18.txt', 'r') as file:

        for line in file.readlines():
            instructions.append(read_inst(line))

    return run(instructions)

print(day18())
