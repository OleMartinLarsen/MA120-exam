#!/usr/bin/python3
import sys

for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    username = line.strip()

    print('{}'.format(username))
