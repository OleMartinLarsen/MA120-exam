#!/usr/bin/python3
import sys
import re
import nltk
from lxml import etree
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

'''parse the data from xml document'''
tree = etree.parse(sys.stdin)
root = tree.getroot()


def clean_text(text):
    '''function for cleaning text'''
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text


def make_bigram(text):
    '''makes a bigrams of a text'''
    tokens = nltk.word_tokenize(text)
    bigram = ngrams(tokens, 2)
    for gram in bigram:
        print('{}\t{}'.format(gram, '1'))


for child in root:
    '''sort on posttype id and extracts title attribute'''
    if child.get('PostTypeId') == '1':
        title = child.get("Title")
        title = clean_text(title)
        title = make_bigram(title)
    
