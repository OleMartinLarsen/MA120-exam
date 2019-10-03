import sys
from collections import OrderedDict
from operator import itemgetter

uniqueWords = []

# input comes from STDIN
for line in sys.stdin:

    # parse the input we got from mapper.py
    # remove leading and trailing whitespace
    # make a list of the strings
    word = line.strip().split()

    # if the word does not already exist in list, add it
    if word not in uniqueWords:
        uniqueWords.append(word)

# remove brackets around items in list
newList = [i[0] for i in uniqueWords]

# print list of unique words
for word in newList:
    print('{}\t'.format(word))
