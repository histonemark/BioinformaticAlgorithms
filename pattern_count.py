#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys


# Assume text is only A,C,T,G

def pattern_count(text,pattern):
    ''' Returns the number of times that pattern is found in text accepting
    overlapped occurrences.'''
    
    count = 0
    texts = len(text)
    patterns = len(pattern)
    indices = texts-patterns

    for i in range(indices):
        if text[i: i + patterns] == pattern:
            count += 1
    print("The kmer was found %d times\n" % count)        
    return count

if __name__ == "__main__":
    text = sys.argv[1]
    pattern = sys.argv[2]
    pattern_count(text,pattern)
