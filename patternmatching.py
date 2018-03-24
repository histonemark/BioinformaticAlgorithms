#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys

#lines = sys.stdin.read().splitlines()
#pattern = lines[0]
#dna = lines[1]

dna = sys.argv[2]
pattern = sys.argv[1]
ldna = len(dna)
lpat = len(pattern)

pos = []

for i in range(ldna - lpat + 1):
    if dna[i: i + lpat] == pattern:
        pos.append(str(i))

print(' '.join(pos))
