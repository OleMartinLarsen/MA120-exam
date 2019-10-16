import sys
from collections import defaultdict
from more_itertools import unique_everseen

word_indexes = defaultdict(list)


for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    word, index = line.strip().split('\t', 1)

    word_indexes[word].append(index)

for word in word_indexes.keys():
    print('{}\t{}'.format(word, ", ".join(
        list(unique_everseen(word_indexes[word])))))
