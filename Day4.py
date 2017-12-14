#!/usr/bin/env python3

def compare_words(word1, word2):

      return bool(not (word1 == word2))

def compare_characters(word1, word2):

    if len(word1) == len(word2):
        print(word1 + ' ' + word2)
        for char in word1:
            if count_character(word1, char) != count_character(word2, char):
                return True
        return False

    return True

def count_character(word, character):

    count = 0
    for char in word:
        if char == character:
            count += 1
    return count

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
print(Day4(compare_characters))
