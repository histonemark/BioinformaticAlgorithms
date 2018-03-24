#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys


def PatternToNumber(pattern):
    symbols = {'A': 0, 'C': 1, 'G':  2, 'T': 3}
    if pattern == '':
        return 0
    symbol = pattern[-1]
    prefix = pattern[:len(pattern) - 1]
    return 4 * PatternToNumber(prefix) + symbols[symbol]

if __name__ == '__main__':
    pattern = sys.argv[1]
    print(PatternToNumber(pattern))
