#!/usr/bin/python3
import sys
from lxml import etree
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter

'''parse the data from xml document'''
tree = etree.parse(sys.stdin)
root = tree.getroot()


def clean_text(text):
    '''function for cleaning text'''
    text = re.sub("<.*?>", '', text.lower())
    text = re.sub(r'[^\w\s]', '', text)
    return text


def make_trigram(text):
    '''makes a trigrams of a text'''
    token = nltk.word_tokenize(text)
    trigram = ngrams(token, 3)
    for gram in trigram:
        print('{}\t{}'.format(gram, '1'))


for child in root:
    '''sort on posttype id and extracts title attribute'''
    if child.get('PostTypeId') == '1':
        title = child.get("Title")
        title = clean_text(title)
        title = make_trigram(title)
