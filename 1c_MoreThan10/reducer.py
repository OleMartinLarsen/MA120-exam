import sys
from collections import OrderedDict
from operator import itemgetter

# counter for how many sentences
counter = 0

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

    # add to the counter for every sentence you get from mapper.py
    # you can do this because the mapper only prints sentences with
    # over 10 words in the title
    counter = counter + count

print('{}'.format(counter))
