import sys


def PatternToNumber(pattern):
    symbols = {'A': 0, 'C': 1, 'G':  2, 'T': 3}
    if pattern == '':
        return 0
    symbol = pattern[-1]
    prefix = pattern[:len(pattern) - 1]
    return 4 * PatternToNumber(prefix) + symbols[symbol]


def NumberToPattern(index, k):
    numtosymbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    if k == 1:
        return numtosymbol[index]
    prefixindex = index // 4
    remainder = index % 4
    prefixpattern = NumberToPattern(prefixindex, k - 1)
    return prefixpattern + numtosymbol[remainder]


def computefreqs(text, k):
    # We initialize the array with 0s
    freq_array = [0 for i in range(4 ** k)]
    # We slide a window of size k updating the freq in the array
    textl = len(text)
    for pos in range(textl - k + 1):
        kmer = text[pos: pos + k]
        freq_array[PatternToNumber(kmer)] += 1
    return freq_array


def clumpfind(genome, k, l, t):
    ''' Find all k-mers generating (l,t)-clumps '''
    freqpatterns = []
    clump_array = [0 for i in range(4 ** k)]

    for i in range(len(genome) - l + 1):
        window = genome[i: i + l]
        kmers_freq = computefreqs(window, k)
        for idx in range(4 ** k):
            if kmers_freq[idx] >= t:
                clump_array[idx] = 1
    for i, kmer in enumerate(clump_array):
        if clump_array[i] == 1:
            kmer = NumberToPattern(i, k)
            if kmer not in freqpatterns:
                freqpatterns.append(kmer)
            return sorted(freqpatterns)

if __name__ == '__main__':
    print(' '.join(clumpfind(sys.argv[1].upper(), int(sys.argv[2]),
                             int(sys.argv[3]), int(sys.argv[4]))))
