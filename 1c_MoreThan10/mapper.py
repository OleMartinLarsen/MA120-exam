#!/usr/bin/python3
import sys
from lxml import etree
import re

'''parse the data from xml document'''
tree = etree.parse(sys.stdin)
root = tree.getroot()


def clean_text(text):
    '''function for cleaning text'''
    text = re.sub("<.*?>", '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = text.strip().split()
    return text


for child in root:
    '''sort on posttype id and extracts title attribute'''
    if child.get('PostTypeId') == '1':
        title = child.get("Title")
        title = clean_text(title)

        '''print titles which have more then 10 words in the title'''
        if len(title) > 10:
            # TODO: Write only one value with null
            print('{}\t{}'.format(title, "1"))
