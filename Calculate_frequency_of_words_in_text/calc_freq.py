#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhjanivijay@gmail.com"
__status__ = "done"

from collections import Counter

file=open("test.txt")

for line in file:
    counts = dict(Counter(line.rstrip().split(' ')))

for key, value in counts.iteritems():
    print key, value 
