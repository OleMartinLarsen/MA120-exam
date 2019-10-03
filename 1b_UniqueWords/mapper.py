import sys
from lxml import etree
import re

sys.stdin = sys.stdin.detach()
tree = etree.parse(sys.stdin)
root = tree.getroot()


def strip_non_ascii(string):
    # Returns the string without non ASCII characters
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


for child in root:
    if child.get("PostTypeId") == "1":
        # extracts the title attribute
        body = child.get("Title")
        # remove tags
        body = re.sub("<.*?>", '', body)
        # remove punctation
        body = re.sub(r'[^\w\s]', '', body)
        body = strip_non_ascii(body)
        # remove leading and trailing whitespace
        # make a list of strings
        words = body.strip().split()

        # print the words you have left after extracting and cleaning the words
        for word in words:
            print('%s' % word.lower())
