#!/usr/bin/env python3

import re

def parse_prog(line):

    prog = dict()

    parts = line.split('->')

    name_weight = re.match('([a-z]+).*\(([0-9]+)\)', parts[0])

    prog['name'] = name_weight.group(1)
    prog['weight'] = int(name_weight.group(2))

    prog['child_names'] = list()
    prog['childs'] = list()
    prog['parent'] = None

    if len(parts) > 1:

        childs = parts[1].replace(" ", "").replace("\n", "").split(',')

        prog['child_names'] = childs


    return prog

def get_prog(progs, name):

    for prog in progs:
        if prog['name'] == name:
            return prog

def get_root(progs):

    for prog in progs:

        for child_name in prog['child_names']:

            child = get_prog(progs, child_name)

            child['parent'] = prog

            prog['childs'].append(child)

    for prog in progs:
        if prog['parent'] == None:
            return prog

def sum_weight(prog):

    weight = prog['weight']
    for child in prog['childs']:
        weight += sum_weight(child)

    prog['weight_sum'] = weight

    return weight

def find_imbalance(progs):

    for prog in progs:

        for child1 in prog['childs']:
            if child1['weight_sum'] != prog['childs'][0]['weight_sum']:

                weight1 = child1['weight_sum']
                weight2 = prog['childs'][0]['weight_sum']
                imbalance = max(weight1, weight2) - min(weight1, weight2)

                return imbalance

def day7():

    progs = list()

    with open('./Input/Day7.txt', 'r') as file:

        for line in file.readlines():

            progs.append(parse_prog(line))

    root = get_root(progs)

    sum_weight(root)

    imbalance = find_imbalance(progs)

    return (root['name'], imbalance)

print(day7())
