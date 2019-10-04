import sys

counter = 0

for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    word, count = line.strip().split('\t', 1)

    try:
        '''convert count (currently a string) to int'''
        count = int(count)
    except ValueError:
        '''count was not a number'''
        continue

    counter = counter + count

print('{}'.format(counter))
