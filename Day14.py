#!/usr/bin/env python3

import Day10

SIZE = 128

def bits(hex_char):
    
    num = int(hex_char, 16)
    
    while num:
        yield bool(num & 0x08)
        num = (num << 1) & 0xff

def count_ones(bit_map, row, hex_string):
    
    ones_count = 0
    
    for char_index, char in enumerate(hex_string):
        for bit_index, bit in enumerate(bits(char)):
            if bit:
                ones_count += 1
                bit_map[(row, (4 * char_index) + bit_index)] = -1
        
    return ones_count
    
def concatenate_regions(regions, region_nr1, region_nr2):
    
    #sets mit region_nr1 und region_nr2
    for region in regions:
        if region_nr1 in region:
            region_set1 = region
        if region_nr2 in region:
            region_set2 = region

    if region_set1 is not region_set2:
        region_set1 |= region_set2
        regions.remove(region_set2)

def count_regions(size, bit_map):
    
    prelim_region_counter = 0
    regions = list()
    
    for row in range(size):
        for column in range(size):
            if bit_map.get((row, column), 0) == -1:
                left = bit_map.get((row, column - 1), 0)
                top = bit_map.get((row - 1, column), 0)
                if left > 0:
                    bit_map[row, column] = left
                    if (top > 0) and (top != left):
                        concatenate_regions(regions, top, left)
                elif top > 0:
                    bit_map[row, column] = top
                else:
                    prelim_region_counter += 1
                    bit_map[row, column] = prelim_region_counter
                    regions.append(set([prelim_region_counter]))
              
    return len(regions)

def Day14(key_string):

    ones_count = 0
    bit_map = dict()

    for row in range(SIZE):
        
        hash_input = key_string + '-' + str(row)
        
        hash = Day10.knot_hash(hash_input)
        
        ones_count += count_ones(bit_map, row, hash)
    
    regions_count = count_regions(SIZE, bit_map)
        
    return (ones_count, regions_count)

print(Day14('jzgqcdpd'))
