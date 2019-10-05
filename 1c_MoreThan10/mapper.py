import sys
from lxml import etree
import re

'''parse the data from xml document'''
sys.stdin = sys.stdin.detach()
tree = etree.parse(sys.stdin)
root = tree.getroot()


def strip_non_ascii(string):
    '''function for stripping non ascii characters from text'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def clean_text(text):
    '''function for cleaning text'''
    text = re.sub("<.*?>", '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = strip_non_ascii(text)
    text = text.strip().split()
    return text


for child in root:
    '''sort on posttype id and extracts title attribute'''
    if child.get('PostTypeId') == '1':
        title = child.get("Title")
        title = clean_text(title)

        '''print titles which have more then 10 words in the title'''
        if len(title) > 10:
            print('{}\t{}'.format(title, "1"))
