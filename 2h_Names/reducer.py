import sys
from collections import OrderedDict
from collections import Counter
from operator import itemgetter

name_count = {}


def top10(data):
    '''sorting names and get top 10 most used'''
    top10 = OrderedDict(
        sorted(data.items(), key=itemgetter(1), reverse=True)[:10])
    return top10


for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    name, count = line.strip().split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        '''count was not a number'''
        continue

    try:
        name_count[name] = name_count[name]+count
    except:
        name_count[name] = count


top10 = top10(name_count)

for name in top10.keys():
    print('{}\t{}'.format(name, name_count[name]))
