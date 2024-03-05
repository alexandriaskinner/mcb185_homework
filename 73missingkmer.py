#73missingkmer.py by Alexandria Skinner

import mcb185
import sys
import itertools

seq = 'AAGACGCC'

def count_kmers(seq, k):
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer]=0
		kcount[kmer] += 1

limit = 1000
for k in range(1, limit):
	kcount = {}
	for aas in itertools.product('AGC', repeat = k):
		kmer = ''.join(aas)
		kcount[kmer] = 0
	
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		forward = mcb185.translate(seq)
		revcomp = mcb185.translate(mcb185.anti_seq(seq))
	
		count_kmers(forward, k)
		count_kmers(revcomp, k)

		stop = 0
		for kmer, n in kcount.items():
			if n == 0:
				print(kmer)
				stop += 1
	if stop >= 1: break
	
	"""
		for i in range(len(seq) -k +1):
			kmer = seq[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
		for i in range(len(seq) -k +1):
			kmer = seq[i:i+k]
			if kmer not in kcount: kcount[kmer] = 0
			kcount[kmer] += 1
		
		'ACDEFGHIKLMNPQRSTVWY'
		"""