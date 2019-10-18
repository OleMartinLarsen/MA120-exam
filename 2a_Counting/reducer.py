#!/usr/bin/python3
import sys

counter = 0

for line in sys.stdin:

    counter = counter + 1

print('{}'.format(counter))
