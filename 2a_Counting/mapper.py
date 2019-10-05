import sys
from lxml import etree
import re

sys.stdin = sys.stdin.detach()
tree = etree.parse(sys.stdin)
root = tree.getroot()


for child in root:
    '''extracts id attribute from user'''
    user_id = child.get("Id")
    # userId = clean_text(userId)

    print('{}'.format(user_id))
