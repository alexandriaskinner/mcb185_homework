#Authors: Alexandria Skinner

import dogma
import sys
import mcb185

file = sys.argv[1]

def kdseq(seq, w):
	"""average kd hydrophobicity for a seq"""
	total = 0
	for aa in seq:
		total += dogma.hydropathy(aa)
	return total / w

def hydrophobic(seq, w, kdval):
	"""determines if there is a hydrophobic region in a protein"""
	for i in range(0, len(seq) -w +1, 1):
		subseq = seq[i:i+w]
		kd = kdseq(subseq, w)
		p = subseq.find('P')
		if kd >= kdval and p == -1:
			return True
			break

for defline, seq in mcb185.read_fasta(file):
	signal = hydrophobic(seq[0:30], 8, 2.5)
	transmembrane = hydrophobic(seq[31:], 11, 2)
	if signal == True and transmembrane = True:
		print(defline[0:60])