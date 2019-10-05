import sys
from statistics import mean
from collections import OrderedDict
from collections import Counter
from operator import itemgetter

answer_counts = {}

for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    question, answer_count = line.strip().split('\t', 1)

    try:
        answer_count = int(answer_count)
    except ValueError:
        '''answer_count was not a number'''
        continue

    answer_counts[question] = answer_count

'''calculates average numbers of answers per question'''
avg_answers = mean(answer_counts.values())

print('{}'.format(avg_answers))
