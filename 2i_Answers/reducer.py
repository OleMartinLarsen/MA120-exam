#!/usr/bin/python3
import sys
from collections import OrderedDict
from collections import Counter
from operator import itemgetter

counter = 0

for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    count = line

    try:
        count = int(count)
    except ValueError:
        '''count was not a number'''
        continue

    counter = counter + count


print('{}'.format(counter))
