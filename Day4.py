#!/usr/bin/env python3

def compare_words(word1, word2):

      return bool(not (word1 == word2))

def Day4(check_words):

    sum = 0
    with open('./Input/Day4.txt', 'r') as file:

        for line in file.readlines():

            count = True
            words = line.split()

            for (index1, word1) in enumerate(words):
              for (index2, word2) in enumerate(words):
                if index1 != index2:
                  if count == True:
                    count = check_words(word1, word2)

            if count != False:
                sum += 1

    return sum

print(Day4(compare_words))
