#!/usr/bin/python3
import sys
from lxml import etree
import re

'''parse the data from xml document'''
sys.stdin = sys.stdin.detach()
tree = etree.parse(sys.stdin)
root = tree.getroot()


def clean_text(text):
    '''function for cleaning text'''
    text = re.sub("<.*?>", '', text)
    text = re.sub(r'[^\w\s]', '', text.lower())
    text = re.sub(r'\w*\d\w*', '', text)
    text = text.strip().split()
    return text


for child in root:
    '''sort on posttype id and extracts body attribute'''
    if child.get("PostTypeId") == '1':
        body = child.get("Body")
        body = clean_text(body)
        for word in body:
            print('{}\t{}'.format(word, "1"))
