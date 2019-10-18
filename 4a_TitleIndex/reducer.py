#!/usr/bin/python3
from more_itertools import unique_everseen
from collections import defaultdict, OrderedDict
import sys

word_indexes = defaultdict(list)


for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    word, index = line.strip().split('\t', 1)

    word_indexes[word].append(index)

word_indexes_sorted = OrderedDict(sorted(word_indexes.items()))

for word in word_indexes_sorted.keys():
    print('{}\t{}'.format(word, ", ".join(
        list(unique_everseen(word_indexes[word])))))
