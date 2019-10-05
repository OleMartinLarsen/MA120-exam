import sys
from lxml import etree
import re

'''parse the data from xml document'''
sys.stdin = sys.stdin.detach()
tree = etree.parse(sys.stdin)
root = tree.getroot()

for child in root:
    '''checks if user has location attribute and extracts it'''
    if child.get('Location') is not None:
        country = child.get('Location')
        print('{}\t{}'.format(country.lower(), "1"))
