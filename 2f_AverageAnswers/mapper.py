import sys
from lxml import etree
import re

'''parse the data from xml document'''
tree = etree.parse(sys.stdin)
root = tree.getroot()

for child in root:
    '''extracts title and answer count attribute from post'''
    if child.get("PostTypeId") == '1':
        question = child.get('Title')
        answer_count = child.get('AnswerCount')

        print('{}\t{}'.format(question, answer_count))
