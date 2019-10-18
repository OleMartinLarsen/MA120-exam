#!/usr/bin/python3
import sys
import re
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

    '''converts string to int'''
    count = int(count)

    try:
        bigram_count[bigram] = bigram_count[bigram]+count
    except:
        bigram_count[bigram] = count

bigram_count = sort_bigrams(bigram_count)

for bigram in bigram_count.keys():
    print('{}\t{}'.format(bigram, bigram_count[bigram]))
