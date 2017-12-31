#! /usr/bin/env python

import math

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
        else:
            print(i)
    
    return h
        
print(day23_opt())
