#!/usr/bin/python3
import sys
from collections import OrderedDict
from operator import itemgetter

bigram_count = {}


def sort_bigrams(data):
    '''sorting the bigram_count by value the key has'''
    sorted_bigram_count = OrderedDict(
        sorted(data.items(), key=itemgetter(1), reverse=True))
    return sorted_bigram_count

for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    bigram, count = line.strip().split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        '''count was not a number'''
        continue

    try:
        bigram_count[bigram] = bigram_count[bigram]+count
    except:
        bigram_count[bigram] = count

bigram_count = sort_words(bigram_count)

for bigram in bigram_count.keys():
    print('{}\t{}'.format(bigram, bigram_count[bigram]))
