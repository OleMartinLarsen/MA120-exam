#!/usr/bin/python3
from nltk.corpus import stopwords
import sys
import re
import nltk
from lxml import etree

'''stopwords imported from natural language toolkit'''
stopwords = set(stopwords.words('english'))

'''parse the data from xml document'''
sys.stdin = sys.stdin.detach()
tree = etree.parse(sys.stdin)
root = tree.getroot()


def remove_stopwords(text):
    '''removes stopwords from text'''
    no_stopwords = [word for word in text
                    if word not in stopwords]
    return no_stopwords


def clean_text(text):
    '''function for cleaning text'''
    text = re.sub(r'[^\w\s]', '', text.lower())
    text = text.strip().split()
    text = remove_stopwords(text)
    return text


for child in root:
    '''sort on posttype id and extracts title attribute'''
    if child.get('PostTypeId') == '1':
        title = child.get('Title')
        title = clean_text(title)
        for word in title:
            print('{}\t{}'.format(word, "1"))
