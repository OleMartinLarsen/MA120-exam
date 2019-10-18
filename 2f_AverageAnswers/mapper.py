#!/usr/bin/python3
import sys
from lxml import etree

'''parse the data from xml document'''
tree = etree.parse(sys.stdin)
root = tree.getroot()

for child in root:
    '''extracts title and answer count attribute from post'''
    if child.get("PostTypeId") == '1':
        answer_count = child.get('AnswerCount')

        print('{}'.format(answer_count))
