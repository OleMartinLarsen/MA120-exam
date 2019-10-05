import sys
from collections import OrderedDict
from collections import Counter
from operator import itemgetter

reputations = {}


def top10(data):
    '''sorting miners and get top 10 based on reputation'''
    top10 = OrderedDict(
        sorted(data.items(), key=itemgetter(1), reverse=True)[:10])
    return top10


for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    username, reputation = line.strip().split('\t', 1)

    try:
        reputation = int(reputation)
    except ValueError:
        '''reputation was not a number'''
        continue

    reputations[username] = reputation


top10 = top10(reputations)

for user in top10.keys():
    print('{}\t{}'.format(user, reputations[user]))
