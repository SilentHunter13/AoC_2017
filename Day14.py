#!/usr/bin/env python3

import Day10

def bits(hex_char):
    
    num = int(hex_char, 16)
    
    while num:
        yield bool(num & 0x08)
        num = (num << 1) & 0xff

def count_ones(hex_string):
    
    ones_count = 0
    
    for char in hex_string:
        for bit in bits(char):
            if bit:
                ones_count += 1
        
    return ones_count

def Day14(key_string):

    ones_count = 0

    for row in range(128):
        
        hash_input = key_string + '-' + str(row)
        
        hash = Day10.knot_hash(hash_input)
        
        ones_count += count_ones(hash)
        
    return ones_count

print(Day14('jzgqcdpd'))
#print(Day14('flqrgnkx'))
