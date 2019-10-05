import sys
from collections import OrderedDict
from collections import Counter
from operator import itemgetter

scores = {}


def top10(data):
    '''sorting questions based on score and get top 10 questions'''
    top10 = OrderedDict(
        sorted(data.items(), key=itemgetter(1), reverse=True)[:10])
    return top10


for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    question, score = line.strip().split('\t', 1)

    try:
        score = int(score)
    except ValueError:
        '''score was not a number'''
        continue

    scores[question] = score


top10 = top10(scores)

for question in top10.keys():
    print('{}\t{}'.format(question, scores[question]))
