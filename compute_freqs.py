  #!/usr/bin/env python
  # -*- coding:utf-8 -*-
  import sys


  def pattern_to_number(pattern):
      symbols = {'A': 0, 'C': 1, 'G':  2, 'T': 3}
      if pattern == '':
          return 0
      symbol = pattern[-1]
      prefix = pattern[:len(pattern) - 1]
      return 4 * pattern_to_number(prefix) + symbols[symbol]


  def compute_freqs(text, k):
      # We initialize the array with 0
      freq_array = [0 for i in range(4 ** k)]
    
      # We slide a window of size k updating the freq in the array
      textl = len(text)
      #kl = len(k)
      for pos in range(textl - k + 1):
          kmer = text[pos : pos + k]
          freq_array[pattern_to_number(kmer)] += 1

      return freq_array

  if __name__ == "__main__":
      str_array = [str(i) for i in compute_freqs(sys.argv[1], int(sys.argv[2]))]
      print(' '.join(str_array))
