import sys
 
word2count = {}
 
for line in sys.stdin:

    line = line.strip()
 
    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    try:
        word2count[word] = word2count[word]+count
    except:
        word2count[word] = count
 
# write the tuples to stdout
# Note: they are unsorted
for word in word2count.keys():
    print('%s\t%s'% ( word, word2count[word] ))
