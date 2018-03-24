#!/usr/bin/env python
# -*- coding:utf-8 -*- 
import sys


def NumberToPattern(index, k):
    numtosymbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    if k == 1:
        return numtosymbol[index]
    prefixindex = index // 4
    remainder = index % 4
    prefixpattern = NumberToPattern(prefixindex, k - 1)
    return prefixpattern + numtosymbol[remainder]

if __name__ == '__main__':
    idx = int(sys.argv[1])
    k = int(sys.argv[2])
    print(NumberToPattern(idx, k))
