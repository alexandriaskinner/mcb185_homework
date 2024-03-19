#80demo.py by Alexandria Skinner

import sys
import json
import mcb185
import dogma
import gzip

"""
print(sys.argv)
print(sys.argv[0])

print(sys.argv[0][1])

matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

print(matrix)
print(matrix[0][1])

person = {
	'name': 'Ali',
	'age': 21,
	'pets': ['Stella', 'Cleo', 'Ray']
}

print(json.dumps(person, indent=4))
print(person['pets'][0])

#curly brackets = object
#square = lists
#usually define structure ahead of time

k = int(sys.argv[2])
kloc = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split()
	chrom = word[0]
	for i in range(len(seq) -k +1):
		kmer = seq[i:i+k]
		if kmer not in kloc: kloc[kmer] = {}
		if chrom not in k\loc{kmer}: kloc[kmer][chrom] = []
		kloc[kmer][chrom].append(i)
print(json.dumps(kloc, indent=4))
"""
"""
Homework:
82: just formatting
83: what is the kozak consensus (nt near the ATG)
	-certain ATGs are facored over others
	-complements have higher number as ATG
	-original seq at end
	-make it look like transfac file
84: 
	-need to flip flop between neg and pos strands
	-can either consider each splice site as occuring once 
	 or weight by how often it is observed at that splice site
"""
"""
#Records:
oligo = {
	'Name': 'SO116',
	'Length': 18,
	'Sequence': 'ATTTAGGTGACACTATAG',
	'Description': 'SP6 promoter sequencing primer'
}

catalog = []
catalog.append(oligo)

catalog = mcb185.read_catalog('../MCB185/data/primers.csv')
for primer in catalog:
	print(primer['Name'], primer['Description'])

catalog = mcb185.read_catalog('../MCB185/data/primers.csv')
for primer in catalog:
	primer['Tm'] = dogma.oligotemp(primer['Sequence'])
print(catalog)

seq = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGT'
k = 2
kloc = {}
for i in range(len(seq) -k +1):
	kmer = seq[i:i+k]
	if kmer not in kloc: kloc[kmer] = []
	kloc[kmer].append(i)
print(kloc)


truc = {
	'animals': {'dog':'woof', 'cat': 'meow', 'pig': 'oink'},
	'numbers': [1.09, 2.72, 3.14],
	'is complete': False,
}

print(json.dumps(truc, indent=4))
"""
"""
introns = [] #or {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		f = line.split()
		if f[2] != 'intron': continue
		chrom = f[0]
		beg = int(f[3]) - 1
		end = int(f[4]) - 1
		strand = f[6]
		n = int(f[5])
		introns.append(chrom, beg, end, strand, n)
"""		
		"""
		if chrom not in introns: introns[chrom] =[]
		introns[chrom].append({
			'beg': beg,
			'end': end,
			'strand': strand,
			'count': n
		})
		"""
"""
for defline, seq, in mcb185.read_fasta(sys.argv[2]):
	words = defline.split()
	chrom = word[0]
	for c, b, e, s, n in introns:
		if chrom == c and s =='+':
			iseq = seq[b:e+1]
			if s = '-': iseq = mcb185.anti_seq(iseq)
			print(iseq[:6], iseq[-6:], s, n)
			don = iseq[:5]
			acc = iseq[-8:]
		print(chrom, beg, )
		
		print(don)
		for i, nt in enumerate(don):
			dons[i][nt] += n #+n accounts for how often each splice site occurred
		for i, nt in enumerate(acc):
			accs[i][nt] += n
"""
#use info to count and make pos weight matrix
#inefficient because going through whole list for each chr, 
#dictionary would be more efficient but not a big difference
"""
#Make empty list of nt counts at each position in donor and acceptor sites
dons = []
accs = []
dlen = 6
aclen = 8

for i in range(dlen):
	dons.append({'A': 0, 'T': 0, 'G': 0, 'C': 0})
for i in range (aclen):
	accs.append({'A': 0, 'T': 0, 'G': 0, 'C': 0})
	
#Change to Transfac format
def print_pwm(ma, id, de, po)
	print('MA', 'at.aac.01')
	print('XX')
	print('ID', kkkk)
	print('XX')
	print('DE', 'yay')
	print('PO')

	for i, n in enumerate(accs):
		a = n['A'] #create variables just for visuals, not necessary
		print(f'{i+1:<8}{a:<8}{c:<8}... )


print('XX')
print('//')

#Float doesn't work on scientific notation
"""
vi hello
#!/bin/env python3

"""
For after the class ends:
-rosalind.info