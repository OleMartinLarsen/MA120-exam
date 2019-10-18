#!/usr/bin/python3
import sys
from collections import OrderedDict
from operator import itemgetter

country_count = {}


def sort_countries(data):
    '''sorting the country_count by value the key has'''
    sorted_countries = OrderedDict(
        sorted(data.items(), key=itemgetter(1), reverse=True))
    return sorted_countries


for line in sys.stdin:

    '''parse the input we got from mapper.py'''
    country, count = line.split('\t', 1)

    '''converts string to int'''
    count = int(count)

    try:
        country_count[country] = country_count[country]+count
    except:
        country_count[country] = count

country_count = sort_countries(country_count)

for country in country_count.keys():
    print('{}\t{}'.format(country, country_count[country]))
