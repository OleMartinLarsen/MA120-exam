import sys
from lxml import etree
import re


sys.stdin = sys.stdin.detach()

# parse the data from xml document
tree = etree.parse(sys.stdin)

# get root node of document
root = tree.getroot()


def strip_non_ascii(string):
    # Returns the string without non ASCII characters
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


for child in root:
    # sorts rows on posttypeid
    if child.get("PostTypeId") == "1":
        # extracts the body attribute
        body = child.get("Title")
        # removes tags
        body = re.sub("<.*?>", '', body)
        # removes punctation
        body = re.sub(r'[^\w\s]', '', body)
        body = strip_non_ascii(body)
        # remove leading and trailing whitespace
        # make a list of strings
        words = body.strip().split()

        # print titles which have more then 10 words in the title
        if len(words) > 10:
            print('{}\t{}'.format(words, "1"))
