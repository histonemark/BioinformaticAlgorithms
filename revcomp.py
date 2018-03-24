#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys


#DNA = sys.stdin.read().rstrip().upper() # Make sure DNA seq is capital
DNA = sys.argv[1].upper()

# Raw and noob implementation without using maketrans or a dict

complement = []
for letter in DNA:
    if letter not in 'ACTG': # check if we are reciving an non DNA input
        print('Non DNA character letter %s' % letter)

    if letter == 'A':
        complement.append('T')
    elif letter == 'T':
        complement.append('A')
    elif letter == 'C':
        complement.append('G')
    else:
        complement.append('C')

revcomplement = complement[::-1]
print(''.join(revcomplement))
