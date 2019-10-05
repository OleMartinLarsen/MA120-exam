import sys
from collections import OrderedDict
from operator import itemgetter

counter = 0

for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    username = line.strip()

    print('{}'.format(username))
