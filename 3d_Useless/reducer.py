#!/usr/bin/python3
import sys
from collections import OrderedDict
from operator import itemgetter

useless_count = 0

for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    count = line

    try:
        count = int(count)
    except ValueError:
        '''count was not a number'''
        continue

    useless_count = useless_count + count

print('{}'.format(useless_count))
