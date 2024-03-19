#83kozak.py by Alexandria Skinner 

import sys
import mcb185
import gzip

chrom = []
coords = []
ft = False
seq = False
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if 'ACCESSION' in line:
			word = line.split()
			ac = word[1]
		
		#Find coordinates of start sites
		if 'FEATURES' in line: ft = True
		if ft != True: continue
		if 'CDS' in line and '/' not in line:
			word = line.split()
			if len(word) < 2: continue
			if 'join' in word[1]: continue
			c = word[1].split('..')
			if 'complement' in line:
				coords.append( [c[0][11:], c[1][0:len(c[1])-1], '-'] )
			else:
				coords.append( [c[0], c[1], '+'] )
	
		#Create chromosome sequence
		if 'ORIGIN' in line: seq = True
		if seq != True: continue
		word = line.split()
		chrom.append(''.join(word[1:]))

chrom = ''.join(chrom)

#Initialize PWM:
pwm = []
for i in range(14):
	pwm.append({'a': 0, 'c': 0, 'g': 0, 't': 0})

for beg, end, s in coords:
	#Get kozak sequence
	if s == '+': 
		kozak = chrom[int(beg)-10:int(beg)+4]
	if s == '-': 
		kozak = mcb185.anti_seq(chrom[int(end)-5:int(end)+9])
	
	#add counts to the pwm
	for i, nt in enumerate(kozak):
		pwm[i][nt] += 1	

#Print PWM
print('AC', ac)
print('XX')
print('ID', 'ECKOZ')
print('XX')
print('DE kozak consensus sequence')
print('PO', 'A ', 'C ', 'G ', 'T ', sep='      ')
for i, d in enumerate(pwm):
	print(f'{i+1:<8}', end='')
	for nt, n in d.items():
		print(f'{n:<8}', end='')
	print()
print('XX')
