#!/usr/bin/python3
import sys
from collections import OrderedDict
from operator import itemgetter

wordcount = {}


def sort_words(data):
    '''sorting the wordcount by value the key has'''
    sorted_wordcount = OrderedDict(
        sorted(data.items(), key=itemgetter(1), reverse=True))
    return sorted_wordcount

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

wordcount = sort_words(wordcount)

for word in wordcount.keys():
    print('{}\t{}'.format(word, wordcount[word]))
