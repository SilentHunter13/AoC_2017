#!/usr/bin/env python3

class Generator:

    def __init__(self, factor, last):
        self.factor = factor
        self.last = last
    
    def generate(self):
        self.last = self.last * self.factor
        self.last = self.last % 2147483647
        return self.last

def day15():

    genA = Generator(16807, 516)
    genB = Generator(48271, 190)
    
    count = 0
    
    for i in range(40000000):
    
        valueA = genA.generate()
        valueB = genB.generate()
        
        if (valueA & 0xffff) == (valueB & 0xffff):
            count += 1
    
    return count

print(day15())
