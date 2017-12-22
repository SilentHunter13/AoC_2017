#!/usr/bin/env python3

def day9():

    sum = 0
    char_count = 0
    groupvalue = 1
    garbage = False
    canceled = False

    with open('./Input/Day9.txt', 'r') as file:

        for char in file.readline():
            #print(groupvalue, garbage, canceled)
            if canceled:
                canceled = False
            else:
                if not garbage:
                    if char == '{':
                        #Anfang Gruppe
                        sum += groupvalue
                        groupvalue += 1
                    elif char == '}':
                        #Ende Gruppe
                        groupvalue -= 1
                    elif char == '<':
                        #Anfang Garbage
                        garbage = True
                else:
                    if char == '>':
                        #Ende Garbage
                        garbage = False
                    elif char == '!':
                        #canceled
                        canceled = True
                    else:
                        print(char)
                        char_count += 1

    return (sum, char_count)


print(day9())
