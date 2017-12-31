#! /usr/bin/env python

import collections

class Turing:

    def __init__(self):
        
        self.tape = collections.defaultdict(bool)
        self.state = self.state_a
        self.cursor = 0
        
    def state_a(self):
        if not self.tape[self.cursor]:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = self.state_b
        else:
            self.tape[self.cursor] = 0
            self.cursor -= 1
            self.state = self.state_c

    def state_b(self):
        if not self.tape[self.cursor]:
            self.tape[self.cursor] = 1
            self.cursor -= 1
            self.state = self.state_a
        else:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = self.state_c
            
    def state_c(self):
        if not self.tape[self.cursor]:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = self.state_a
        else:
            self.tape[self.cursor] = 0
            self.cursor -= 1
            self.state = self.state_d
            
    def state_d(self):
        if not self.tape[self.cursor]:
            self.tape[self.cursor] = 1
            self.cursor -= 1
            self.state = self.state_e
        else:
            self.tape[self.cursor] = 1
            self.cursor -= 1
            self.state = self.state_c
            
    def state_e(self):
        if not self.tape[self.cursor]:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = self.state_f
        else:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = self.state_a
            
    def state_f(self):
        if not self.tape[self.cursor]:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = self.state_a
        else:
            self.tape[self.cursor] = 1
            self.cursor += 1
            self.state = self.state_e
        
    def run(self):
        
        for i in range(12134527): #12134527
            self.state()
            #print(self.state, self.tape)
            
        ones = 0
        for k in self.tape.keys():
            if self.tape[k]:
                ones += 1
        
        return ones

def day25():
    
    turing = Turing()
    return turing.run()



print(day25())
