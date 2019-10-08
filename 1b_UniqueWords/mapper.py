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
    text = strip_non_ascii(text)
    text = text.strip().split()
    return text


for child in root:
    '''sort on posttype id and extracts title attribute'''
    if child.get('PostTypeId') == '1':
        title = child.get("Title")
        title = clean_text(title)

        for word in title:
            print('{}'.format(word))
