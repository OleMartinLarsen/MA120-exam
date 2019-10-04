import sys

counter = 0

for line in sys.stdin:

    word, count = line.strip().split('\t', 1)

    try:
        '''convert count (currently a string) to int'''
        count = int(count)
    except ValueError:
        continue

    counter = counter + count

print('{}'.format(counter))
