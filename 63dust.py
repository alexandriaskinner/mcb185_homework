#Author: Alexandria Skinner

import sys
import math
import mcb185

def entropy(seq):
	"""returns entropy for a given sequence"""
	pa = 0
	pt = 0
	pg = 0
	pc = 0
	prob = []
	h = 0
	for nt in seq:
		if nt == 'A': pa += (1/len(seq))
		if nt == 'T': pt += (1/len(seq))
		if nt == 'G': pg += (1/len(seq))
		if nt == 'C': pc += (1/len(seq))
	if pa > 0: prob.append(pa)
	if pt > 0: prob.append(pt)
	if pg > 0: prob.append(pg)
	if pc > 0: prob.append(pc)
	for p in prob:
		h -= p * math.log2(p)
	return h

file = sys.argv[1]
w = int(sys.argv[2])
threshhold = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(file):
	sequence = list(seq)
	n = []
	for i in range(0, len(sequence) -w +1, 1):
		subseq = sequence[i:i+w]
		h = entropy(subseq)
		if h < threshhold:
			for j in range(0,w):
				n.append(i+j)

	for pos in n:
		sequence[pos] = 'N'
	filtered = ''.join(sequence)

	print(defline)
	for i in range(0, len(filtered), 60):
		print(filtered[i:i+60])