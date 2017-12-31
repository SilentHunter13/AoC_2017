#! /usr/bin/env python

def get_strength(bridge):
    strength = 0
    
    for element in bridge:
        strength += element[0]
        strength += element[1]
    
    return strength

def get_matching(elements, port):

    return [element for element in elements if (element[0] == port) or (element[1] == port)]

def get_free_port(bridge):

    free_port = 0
    if len(bridge) == 1:
        free_port = max(bridge[-1])
    else:
        if bridge[-1][0] not in bridge[-2]:
            free_port = bridge[-1][0]
        else:
            free_port = bridge[-1][1]
    
    return free_port


def create_bridges(elements):

    bridges = list()
    #Startpunkte finden
    for element in get_matching(elements, 0):
        bridge = list()
        bridge.append(element)
        bridges.append(bridge)

    #Brücken bauen
    for bridge in bridges:
        free_port = get_free_port(bridge)
        for match in get_matching(elements, free_port):
            if match not in bridge:
                newbridge = list(bridge)
                newbridge.append(match)
                bridges.append(newbridge)

    return bridges

def day24():

    elements = list()

    with open('./Input/Day24.txt', 'r') as file:

        for line in file.readlines():
            ports = line.split('/')
            elements.append((int(ports[0]), int(ports[1])))

    bridges = create_bridges(elements)
    
    longest_length = len(max(bridges, key=len))
    
    longest_bridges = [e for e in bridges if len(e) == longest_length]
    
    return (get_strength(max(bridges, key=get_strength)), get_strength(max(longest_bridges, key=get_strength)))


print(day24())
