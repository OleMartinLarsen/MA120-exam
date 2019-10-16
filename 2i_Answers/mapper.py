#!/usr/bin/python3
import sys
from lxml import etree
import re

'''parse the data from xml document'''
tree = etree.parse(sys.stdin)
root = tree.getroot()

for child in root:
    '''extracts title attribute from post to
    questions with more than 0 answers'''
    if child.get('PostTypeId') == '1' and child.get('AnswerCount') != '0':

        print('{}'.format('1'))
