from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import sys

for line in sys.stdin:

    title = line.strip()
    print(title)
