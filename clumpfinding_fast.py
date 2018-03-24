import sys
import pdb


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


def fastclumpfind(genome, k, l, t):

    freqpatterns = []
    allkmers = range(4 ** k)
    clump_array = [0 for i in allkmers]

    # Generate freq-array for the first window and search for clumps
    # pdb.set_trace()
    window = genome[0:l]
    kmers_freq = computefreqs(window, k)
    for i in allkmers:
        if kmers_freq[i] >= t:
            clump_array[i] = 1

    # Slide a window len l and update freq_array
    for i in xrange(1, len(genome) - l):
        firstkmer = genome[i: i + k]
        fidx = PatternToNumber(firstkmer)
        kmers_freq[fidx] -= 1
        lastkmer = genome[i + l - k: i + l]
        lidx = PatternToNumber(lastkmer)
        kmers_freq[lidx] += 1
        if kmers_freq[fidx] >= t:
            clump_array[fidx] = 1
        if kmers_freq[lidx] >= t:
            clump_array[lidx] = 1

    for i in allkmers:
        if clump_array[i] == 1:
            kmer = NumberToPattern(i, k)
            if kmer not in freqpatterns:
                freqpatterns.append(kmer)

    return sorted(freqpatterns)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        genome = f.readline().rstrip()
        k, l, t = f.readline().split()
        clumps = ' '.join(fastclumpfind(genome, int(k), int(l), int(t)))
        print(clumps)
    # print(' '.join(fastclumpfind(sys.argv[1].upper(), int(sys.argv[2]),
    #                              int(sys.argv[3]), int(sys.argv[4]))))
