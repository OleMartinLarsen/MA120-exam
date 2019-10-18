#!/usr/bin/python3
import sys
from statistics import mean

answer_counts = []

for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    answer_count = line.strip()

    try:
        answer_count = int(answer_count)
    except ValueError:
        '''answer_count was not a number'''
        continue

    answer_counts.append(answer_count)

'''calculates average numbers of answers per question'''
avg_answers = mean(answer_counts)

print('{}'.format(avg_answers))
