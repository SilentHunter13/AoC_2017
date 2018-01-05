#!/usr/bin/env python3

STEPS = 377

def get_after_current(iterations):
    buffer = [0]
    next_value = 1
    current_position = 0

    while next_value < iterations:
        current_position = (current_position + STEPS) % len(buffer) + 1

        buffer.insert(current_position, next_value)
        next_value += 1

    return buffer[current_position + 1]

def get_after_zero(iterations):
    next_value = 1
    current_position = 0
    buffer_len = 1

    while next_value < iterations:
        current_position = (current_position + STEPS) % buffer_len + 1

        if current_position == 1:
            after_zero = next_value

        buffer_len += 1
        next_value += 1

    return after_zero

def day17():

    return (get_after_current(2018), get_after_zero(50000000))

print(day17())
