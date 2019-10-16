#!/usr/bin/python3
import sys

uniqueWords = []

for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    word = line.strip().split()

    '''if the word does not already exist in list, add it'''
    if word not in uniqueWords:
        uniqueWords.append(word)

'''remove brackets around words'''
newList = [i[0] for i in uniqueWords]

for word in newList:
    print('{}\t'.format(word))
