import sys
from lxml import etree
import re

sys.stdin = sys.stdin.detach()
tree = etree.parse(sys.stdin)
root = tree.getroot()


def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


for child in root:
    if child.get("PostTypeId") == "1":
        body = child.get("Title")
        body = re.sub("<.*?>", '', body)
        body = re.sub(r'[^\w\s]', '', body)
        body = strip_non_ascii(body)
        words = body.strip().split()

        for word in words:
            print('%s\t%s' % (word.lower(), "1"))
