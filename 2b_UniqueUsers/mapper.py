import sys
from lxml import etree
import re

'''parse the data from xml document'''
sys.stdin = sys.stdin.detach()
tree = etree.parse(sys.stdin)
root = tree.getroot()


def strip_non_ascii(string):
    '''function for stripping non ascii characters from text'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


for child in root:
    '''extracts id attribute from user'''
    username = child.get("DisplayName")
    username = strip_non_ascii(username)

    print('{}'.format(username))
