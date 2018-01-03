#!/usr/bin/env python3

class Generator:

    def __init__(self, factor, last):
        self.factor = factor
        self.last = last
    
    def generate(self):
        self.last = self.last * self.factor
        self.last = self.last % 2147483647
        return self.last
        
class PickyGenerator(Generator):

    def __init__(self, factor, last, divisor):
        super().__init__(factor, last)
        self.divisor = divisor
        
    def generate(self):
        value = super().generate()
        while value % self.divisor != 0:
            value = super().generate()
        return value
        
class Judge:
    
    def __init__(self, genA, genB):
        self.genA = genA
        self.genB = genB
    
    def judge(self, pairs):
    
        count = 0
    
        for i in range(pairs):
    
            valueA = self.genA.generate()
            valueB = self.genB.generate()
        
            if (valueA & 0xffff) == (valueB & 0xffff):
                count += 1
                
        return count

def day15():

    #genA = Generator(16807, 65)
    #genB = Generator(48271, 8921)
    genA = Generator(16807, 516)
    genB = Generator(48271, 190)
    
    judge1 = Judge(genA, genB)
    
    #genA_picky = PickyGenerator(16807, 65, 4)
    #genB_picky = PickyGenerator(48271, 8921, 8)
    genA_picky = PickyGenerator(16807, 516, 4)
    genB_picky = PickyGenerator(48271, 190, 8)
    
    judge2 = Judge(genA_picky, genB_picky)
    
    return (judge1.judge(40000000), judge2.judge(5000000))

print(day15())
