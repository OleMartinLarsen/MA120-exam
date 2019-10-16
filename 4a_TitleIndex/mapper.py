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
    '''extracts title of questions and the body/extracts the body of answers'''
    if child.get('Title') is not None:
        title = child.get("Title")
        title = clean_text(title)
        body = child.get("Body")
        body = clean_text(body)
        row_text = title + body
        for word in row_text:
            print('{}\t{}'.format(word, child.get('Id')))
    else:
        body = child.get("Body")
        body = clean_text(body)
        for word in body:
            print('{}\t{}'.format(word, child.get('Id')))
