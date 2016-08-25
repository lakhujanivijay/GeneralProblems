#!/usr/bin/python3
__author__ = "Vijay Lakhujani"
__credits__ = ["Vijay Lakhujani"]
__version__ = "1.0"
__email__ = "lakhjanivijay@gmail.com"
__status__ = "done"

import getopt,sys

from itertools import permutations

num_list=[]

count=0

try:
    options, remainder=getopt.getopt(sys.argv[1:], 'i:n:')

except getopt.GetoptError as err:
    print str(err)
    sys.exit()

for opt, arg in options:
    if opt in ('-i'):
        input_file=arg
    elif opt in ('-n'):
        number=int(arg)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if number<=7:
   print factorial(number)
   for i in range(1,number+1):
       num_list.append(str(i))
   for p in permutations(num_list):
       print ' '.join(p)

else:
    print "Error: Input number should be <=7"
