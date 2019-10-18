#!/usr/bin/python3
import sys
from lxml import etree

'''parse the data from xml document'''
tree = etree.parse(sys.stdin)
root = tree.getroot()

for child in root:
    '''checks if user has location attribute and extracts it'''
    if child.get('Location') is not None:
        country = child.get('Location')
        print('{}\t{}'.format(country.lower(), "1"))
