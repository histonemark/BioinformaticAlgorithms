#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from collections import defaultdict

#text,k = sys.stdin.read().splitlines()
text = sys.argv[1]
k = sys.argv[2]

k = int(k)
kmers = defaultdict(int)
texts = len(text)
indices = texts - k + 1

for i in range(indices):
    kmer = text[i: i + k]
    kmers[kmer] += 1


sorted_kmers = sorted(kmers.items(), key=lambda kv: (kv[1], kv[0]))
max_kmer  = sorted_kmers.pop()
max_kmers = [max_kmer[0]]
    
for i in range(len(sorted_kmers) - 1):
    next_kmer = sorted_kmers.pop()
        
    if int(next_kmer[1]) == int(max_kmer[1]):
        max_kmers.append(next_kmer[0])
        max_kmer = next_kmer
else:
    print(" ".join(max_kmers[::-1]))
