import sys
from collections import OrderedDict
from operator import itemgetter

wordcount = {}

for line in sys.stdin:

    # parse the input we got from mapper.py
    # remove leading and trailing whitespace
    # make a list of the strings
    word, count = line.strip().split('\t', 1)
    try:
        # convert count (currently a string) to int
        count = int(count)
    except ValueError:
        # count was not a number
        # ignore/discard this line
        continue

    try:
        # if multiple words add then count together
        # this is made possible becuase sorts the map output by key before
        # passed to the reducer
        wordcount[word] = wordcount[word]+count
    except:
        wordcount[word] = count


# sorting the wordcount by value
wordcount = OrderedDict(
    sorted(wordcount.items(), key=itemgetter(1), reverse=True))

# printing the wordcount
for word in wordcount.keys():
    print('%s\t%s' % (word, wordcount[word]))
