#!/usr/bin/python3
import sys
from lxml import etree
import re

'''parse the data from xml document'''
tree = etree.parse(sys.stdin)
root = tree.getroot()

for child in root:
    '''extracts title and score attribute from post'''
    if child.get("PostTypeId") == '1':
        question = child.get('Title')
        score = child.get('Score')

        print('{}\t{}'.format(question, score))
