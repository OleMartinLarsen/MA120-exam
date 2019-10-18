#!/usr/bin/python3
import sys

counter = 0

for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    count = line

    count = int(count)

    counter = counter + count


print('{}'.format(counter))
