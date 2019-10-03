import sys
from collections import OrderedDict
from operator import itemgetter

wordcount = {}

for line in sys.stdin:

    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    try:
        wordcount[word] = wordcount[word]+count
    except:
        wordcount[word] = count

wordcount = OrderedDict(
    sorted(wordcount.items(), key=itemgetter(1), reverse=True))

for word in wordcount.keys():
    print('%s\t%s' % (word, wordcount[word]))
