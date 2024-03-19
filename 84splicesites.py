#84splicesites.py by Alexandria Skinner

import sys
import mcb185
import json
import gzip

fasta = sys.argv[1]
gff = sys.argv[2]

def print_pwm(pwm, ac, id, de):
	print('AC', ac)
	print('XX')
	print('ID', id)
	print('XX')
	print('DE', de)
	print('PO', 'A ', 'C ', 'G ', 'T ', sep='      ')
	for i, d in enumerate(pwm):
		print(f'{i+1:<8}', end='')
		for nt, n in d.items():
			print(f'{n:<8}', end='')
		print()
	print('XX')
	print('//')

#add seq to a library
chrom = {}
for defline, seq in mcb185.read_fasta(fasta):
	chrid = defline.split()[0]
	chrom[chrid] = seq

#Find intron positions:
introns = []
with gzip.open(gff, 'rt') as fp:
	for line in fp:
		f = line.split('\t')
		c = f[0]
		ft  = f[2]
		beg = int(f[3]) -1
		end = int(f[4]) -1
		n = f[5]
		s = f[6]
		
		if n == '.': continue
		else: n = float(n)
		
		if ft != 'intron': continue
		introns.append( (c, beg, end, n, s))

#Initialize PWMs:
don = []
for i in range(6):
	don.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

acc = []
for i in range(8):
	acc.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

#Find sequences of splice sites:
for c, beg, end, n, s in introns:
	if s == '+': iseq = chrom[c][beg:end+1]
	else:        iseq = mcb185.anti_seq(chrom[c][beg:end+1])
	
	dseq = iseq[0:6]
	for i, nt in enumerate(dseq):
		don[i][nt] += n
	
	aseq = iseq[-8:]
	for i, nt in enumerate(aseq):
		acc[i][nt] += n

print_pwm(acc, 'int01', 'ACC', 'splice acceptor')
print_pwm(don, 'int02', 'DON', 'donor site')