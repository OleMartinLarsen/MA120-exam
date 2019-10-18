#!/usr/bin/python3
import sys

useless_count = 0

for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    count = line

    count = int(count)

    useless_count = useless_count + count

print('{}'.format(useless_count))
