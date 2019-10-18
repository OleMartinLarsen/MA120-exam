#!/usr/bin/python3
import sys
from lxml import etree

'''parse the data from xml document'''
tree = etree.parse(sys.stdin)
root = tree.getroot()

for child in root:
    '''check if questions has more than 1 answer'''
    if child.get('PostTypeId') == '1' and child.get('AnswerCount') is not '0':

        print('{}'.format('1'))
