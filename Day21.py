#!/usr/bin/env python3

import numpy as np

def flip(matrix):

    return matrix[::-1,:]

class Rule:

    def __init__(self, line):

        parts = line.strip().split(' => ')
        size = len(parts[0].split('/')[0])

        input = parts[0].replace('/', '')
        input = input.replace('#','1')
        input = input.replace('.','0')

        self._input = np.array(list(input), dtype=int)
        self._input.shape = (size, size)

        output = parts[1].replace('/', '')
        output = output.replace('#','1')
        output = output.replace('.','0')
        self._output = np.array(list(output), dtype=int)
        self._output.shape = (size + 1, size + 1)

    def __repr__(self):

        repr = 'i=\n{0};\n o=\n{1}\n'.format(self._input, self._output)

        return repr

    def get_enhanced(self, old):

        out = None
        #print('Start\n')
        #print(old)
        if old.shape == self._input.shape:
            for i in range(4):
                rot_input = np.rot90(self._input, i)
                #print(rot_input)
                if (old == rot_input).all():
                    out = self._output


                #print(flip(rot_input))
                if (old == flip(rot_input)).all():
                    out = self._output
        #print('End\n')
        #print(out)
        return out

def enhance(canvas, rules):

    if canvas.shape[0] % 2 == 0:
        step = 2
        square_count = canvas.shape[0] // 2
    else:
        step = 3
        square_count = canvas.shape[0] // 3

    new_canvas = np.zeros((square_count*(step + 1),square_count*(step + 1)))

    for i in range(square_count):
        for j in range(square_count):

            old_square = canvas[i*step:(i+1)*step,j*step:(j+1)*step]

            for rule in rules:

                new_square = rule.get_enhanced(old_square)

                if new_square is not None:
                    new_canvas[i*(step+1):(i+1)*(step+1),j*(step+1):(j+1)*(step+1)] = new_square
                    break

    return new_canvas



def day21():

    rules = list()

    with open('./Input/Day21.txt', 'r') as file:

        for line in file.readlines():
            rules.append(Rule(line))

    canvas = np.array(list('010/001/111'.replace('/', '')), dtype=int)
    canvas.shape = (3, 3)

    for i in range(18):
        canvas = enhance(canvas, rules)

    return np.sum(canvas)

print(day21())
