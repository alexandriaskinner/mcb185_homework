#Author: Alexandria Skinner

import dogma
import sys
import mcb185

def profinder(seq, min):
	proteins = []
	for orf in dogma.translate(seq).split('*'):
		if 'M' in orf: 
			start = orf.find('M')
			protein = orf[start:]
			if len(protein) >= min:
				proteins.append(protein)
	return proteins

file = sys.argv[1]
min = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(file):
	seqid = defline.split()
	id = 0
	for frame in range(3):
		for protein in profinder(seq[frame:], min):
			id += 1
			print(f'{seqid[0]}-prot-{id}\n{protein}')
		for protein in profinder(dogma.revcomp(seq[frame:]), min):
			id += 1
			print(f'{seqid[0]}-prot-{id}\n{protein}')
