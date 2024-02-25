#Author: Alexandria Skinner

import sys
import mcb185
"""
for defline, seq in mcb185.read_fasta(sys.argv[1]): 
	print(defline[:30], seq[:40], len(seq))

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0
	for nt in seq:
		if nt == 'C' or nt == 'G': gc += 1
	print(name, gc/len(seq))
"""
nts = 'ACGTN'
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	#counts = [0] * len(nts)
	print(name, end='\t')
	for nt in nts:
		print(seq.count(nt) / len(seq), end='\t')
	print()
