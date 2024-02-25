#Author: Alexandria Skinner

import dogma
import sys
import mcb185

#seq = 'ACGTACGTGGGGGACGTACGTCCCCC'

file = sys.argv[1]
w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(file):
	for i in range(len(seq) -w +1):
		s = seq[i:i+w]
		print(i, dogma.gc_comp(s), dogma.gc_skew(s))