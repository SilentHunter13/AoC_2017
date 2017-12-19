#!/usr/bin/env python3

def inc_index(index, size):
    index += 1

    if index >= size:
        index = 0

    return index

def day6():

    banks = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]

    history = list()

    steps = 0

    while banks not in history:

        history.append(list(banks))

        value_to_share = max(banks)

        act_index = banks.index(value_to_share)

        banks[act_index] = 0

        act_index = inc_index(act_index, len(banks))

        while value_to_share > 0:
            banks[act_index] += 1
            act_index = inc_index(act_index, len(banks))
            value_to_share -= 1

        steps += 1

    loop_size = steps - history.index(banks)
    return (steps, loop_size)

print(day6())
