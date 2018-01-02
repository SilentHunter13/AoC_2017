#!/usr/bin/env python3

LIST_LENGTH = 256

def day10_p1(lengths):
    
    old_list = range(LIST_LENGTH)
    current_position = 0
    skip_size = 0
    
    for length in lengths:
        
        new_list = list(old_list)
        for i in range(length):
            old_position = (current_position + i) % LIST_LENGTH
            new_position = (current_position + length - 1 - i) % LIST_LENGTH
            new_list[new_position] = old_list[old_position]
        
        old_list = new_list
        current_position += length + skip_size
        skip_size += 1
            
    return old_list[0] * old_list[1]
    
def knot_hash(string):

    lengths = [ord(x) for x in string]
    
    lengths += [17, 31, 73, 47, 23]
    
    old_list = range(LIST_LENGTH)
    current_position = 0
    skip_size = 0
    
    for _ in range(64):
        for length in lengths:
        
            new_list = list(old_list)
            for i in range(length):
                old_position = (current_position + i) % LIST_LENGTH
                new_position = (current_position + length - 1 - i) % LIST_LENGTH
                new_list[new_position] = old_list[old_position]
        
            old_list = new_list
            current_position += length + skip_size
            skip_size += 1
        
    dense_hash = ''
    
    for byte_index in range(16):
    
        dense_hash_byte = 0
    
        for index in range(16):
        
            dense_hash_byte ^= old_list[(16 * byte_index) + index]
        
        dense_hash += '{:02x}'.format(dense_hash_byte)
    
    return dense_hash

print(day10_p1([147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70]))
print(knot_hash('147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70'))
