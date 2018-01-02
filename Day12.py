#!/usr/bin/env python3

def decode_connection(groups, line):

    parts = line.split('<->')

    partners = parts[1].split(',')
    
    partners.append(parts[0])
    
    groups.append(frozenset([int(x) for x in partners]))

def day12():

    groups = list()

    with open('./Input/Day12.txt', 'r') as file:

        for line in file.readlines():
            decode_connection(groups, line)

    ready = False

    while not ready:
        ready = True
        for group1 in groups:
            for group2 in [x for x in groups if group1 is not x]:
                if not group1.isdisjoint(group2):
                    index1 = groups.index(group1)
                    groups[index1] = group1.union(group2)
                    group1 = group1.union(group2)
                    del(groups[groups.index(group2)])
                    ready = False
    
    for group in groups:
        if 0 in group:
            group0_length = len(group)
    
    return (group0_length, len(groups))

print(day12())
