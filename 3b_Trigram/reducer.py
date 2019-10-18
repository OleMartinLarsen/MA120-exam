#!/usr/bin/python3
import sys
from collections import OrderedDict
from operator import itemgetter

trigram_count = {}


def sort_trigrams(data):
    '''sorting the trigram_count by value the key has'''
    sorted_trigram_count = OrderedDict(
        sorted(data.items(), key=itemgetter(1), reverse=True))
    return sorted_trigram_count

for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    trigram, count = line.strip().split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        '''count was not a number'''
        continue

    try:
        trigram_count[trigram] = trigram_count[trigram]+count
    except:
        trigram_count[trigram] = count


trigram_count = sort_words(trigram_count)

for trigram in trigram_count.keys():
    print('{}\t{}'.format(trigram, trigram_count[trigram]))
