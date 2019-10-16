#!/usr/bin/python3
import sys
from collections import OrderedDict
from collections import Counter
from operator import itemgetter

favorite_counts = {}


def top10(data):
    '''sorting questions based on favorite count and get top 10 questions'''
    top10 = OrderedDict(
        sorted(data.items(), key=itemgetter(1), reverse=True)[:10])
    return top10


for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    question, favorite_count = line.strip().split('\t', 1)

    try:
        favorite_count = int(favorite_count)
    except ValueError:
        '''favorite_count was not a number'''
        continue

    favorite_counts[question] = favorite_count


top10 = top10(favorite_counts)

for question in top10.keys():
    print('{}\t{}'.format(question, favorite_counts[question]))
