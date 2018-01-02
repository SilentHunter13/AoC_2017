#!/usr/bin/env python3

def day10(elements, lengths):
    
    old_list = range(elements)
    current_position = 0
    skip_size = 0
    
    for length in lengths:
        
        new_list = list(old_list)
        for i in range(length):
            old_position = (current_position + i) % elements
            new_position = (current_position + length - 1 - i) % elements
            new_list[new_position] = old_list[old_position]
        
        old_list = new_list
        current_position += length + skip_size
        skip_size += 1
            
    return old_list[0] * old_list[1]

print(day10(256, [147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70]))
