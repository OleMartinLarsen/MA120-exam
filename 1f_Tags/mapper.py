import sys
from lxml import etree
import re

'''parse the data from xml document'''
sys.stdin = sys.stdin.detach()
tree = etree.parse(sys.stdin)
root = tree.getroot()


def clean_text(text):
    '''function for cleaning text'''
    text = re.sub("<", ' ', text)
    text = re.sub(">", ' ', text)
    text = text.strip().split()
    return text


for child in root:
    '''sort on posttype id and extracts body attribute'''

    if child.get("Tags") is not None:
        tags = child.get("Tags")
        tags = clean_text(tags)
        for tag in tags:
            print('{}'.format(tag))
