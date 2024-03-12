#73missingkmer.py by Alexandria Skinner

import mcb185
import sys
import itertools

def count_kmers(seq, k):
	for i in range(len(seq)-k+1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 0
		kcount[kmer] += 1

limit = 1000
for k in range(1, limit):
	kcount = {}
	missingkmers = 0
	
	#Create dictionary of kmers of length k
	for aas in itertools.product('ACGT', repeat = k):
		kmer = ''.join(aas)
		kcount[kmer] = 0
		
	#Count kmers in the sequence
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		count_kmers(seq, k)
		count_kmers(mcb185.anti_seq(seq), k)

	#Check for kmers that aren't found in the sequence
	stop = False
	for kmer, n in kcount.items():
		if n == 0:
			stop = True
			missingkmers += 1
	if stop == True: 
		print(f'For k = {k}, there are {missingkmers} missing kmers.')
		break