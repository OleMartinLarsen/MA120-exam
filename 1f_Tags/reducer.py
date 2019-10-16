#!/usr/bin/python3
import sys

unique_tags = []

for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    tag = line.strip().split()

    '''if the tag does not already exist in list, add it'''
    if tag not in unique_tags:
        unique_tags.append(tag)

'''remove brackets around words'''
new_list = [i[0] for i in unique_tags]

for tag in new_list:
    print('{}\t'.format(tag))
