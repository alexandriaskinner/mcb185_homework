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
introns = {}
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		f = line.split()
		if f[2] != 'intron': continue
		chrom = f[0]
		beg = int(f[3]) - 1
		end = int(f[4]) - 1
		strand = f[6]
		n = int(f[5])
		#print(chrom, beg, end, strand, n)
		if chrom not in introns: introns[chrom] =[]
		introns[chrom].append({
			'beg': beg,
			'end': end,
			'strand': strand,
			'count': n
		})
print(json.dumps(introns, indent=4))