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

#Sliding Windows Algorithms
w = 10
s = 1
for i in range(0, len(seq) -w +1, s):
	subseq = seq[i:i+w]

#In Class Notes:
"""
str.split()
str.join()    variable before funtion -- object syntax
str.count()

len()         variable after function
print()

math.log2() is not object syntax

s = 'GATC' is string
l = [G, A, T] is a list