#!/usr/bin/python3
import sys
from lxml import etree
import re

'''parse the data from xml document'''
tree = etree.parse(sys.stdin)
root = tree.getroot()

for child in root:
    '''extracts displayname and reputation attribute from user'''
    name = child.get('DisplayName')

    print('{}\t{}'.format(name, '1'))
