#!/usr/bin/python3
import sys
from lxml import etree
import re

'''parse the data from xml document'''
tree = etree.parse(sys.stdin)
root = tree.getroot()

for child in root:
    '''extracts title and favourite count attribute from post'''
    if child.get("PostTypeId") == '1':
        question = child.get('Title')
        favourite_count = child.get('FavoriteCount')

        print('{}\t{}'.format(question, favourite_count))
