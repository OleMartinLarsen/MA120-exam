#!/usr/bin/python3
import sys
from collections import OrderedDict
from operator import itemgetter

wordcount = {}

for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    word, count = line.strip().split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        '''count was not a number'''
        continue

    try:
        wordcount[word] = wordcount[word]+count
    except:
        wordcount[word] = count


'''sorting the wordcount by value the key has'''
wordcount = OrderedDict(
    sorted(wordcount.items(), key=itemgetter(1), reverse=True))

for word in wordcount.keys():
    print('{}\t{}'.format(word, wordcount[word]))
