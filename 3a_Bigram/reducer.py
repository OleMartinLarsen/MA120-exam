#!/usr/bin/python3
import sys
from collections import OrderedDict
from operator import itemgetter

bigram_count = {}

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


'''sorting the bigram_count by value the key has'''
bigram_count = OrderedDict(
    sorted(bigram_count.items(), key=itemgetter(1), reverse=True))

for bigram in bigram_count.keys():
    print('{}\t{}'.format(bigram, bigram_count[bigram]))
