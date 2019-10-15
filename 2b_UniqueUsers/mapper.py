import sys
from lxml import etree
import re

'''parse the data from xml document'''
tree = etree.parse(sys.stdin)
root = tree.getroot()

for child in root:
    '''extracts id attribute from user'''
    username = child.get("DisplayName")

    print('{}'.format(username))
