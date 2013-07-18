from __future__ import print_function
import re

filename='test.txt'
pattern=r'\bNaN\b'

with open(filename,'r') as f:
    stuff=f.readlines()

    for i,lines in enumerate(stuff[::-1]):
        match=re.search(pattern,lines)
        if match:
            print(i,lines)
            print(match.group(0))
            break
