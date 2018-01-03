#!/usr/bin/env python3

def got_caught(depth, range):
    
    steps = 2 * (range - 1)
    
    return bool(depth % steps == 0)
    
def calc_severity(scanners):
       
    severity = 0   
       
    for scanner in scanners:
        if got_caught(scanner['depth'], scanner['range']):
            severity += scanner['depth'] * scanner['range']
    
    return severity
    
def day13():

    scanners = list()
    
    
    with open('./Input/Day13.txt', 'r') as file:

        for line in file.readlines():
            parts = line.split(':')
            
            scanner = {'depth': int(parts[0]), 'range': int(parts[1])}
            scanners.append(scanner)
                
    return calc_severity(scanners)
            
print(day13())
