#Author: Alexandria Skinner

def transcribe(dna):
	#converts 'T' to 'U'
	return dna.replace('T', 'U')

def revcomp(dna):
	#returns reverse complement of a sequence
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc)

def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		c = dna[i:i+3]
		if   c == 'ATG':                             aas.append('M')
		elif c == 'TTT' or c == 'TTC':               aas.append('F')
		elif c == 'TTA' or c == 'TTG' or c == 'CTT': aas.append('L')
		elif c == 'CTC' or c == 'CTA' or c == 'CTG': aas.append('L')
		elif c == 'ATT' or c == 'ATC' or c == 'ATA': aas.append('I')
		elif c == 'GTT' or c == 'GTC' or c == 'GTA': aas.append('V')
		elif c == 'GTG':                             aas.append('V')
		elif c == 'TCT' or c == 'TCC' or c == 'TCA': aas.append('S')
		elif c == 'TCG':                             aas.append('S')
		elif c == 'CCT' or c == 'CCC' or c == 'CCA': aas.append('P')
		elif c == 'CCG':                             aas.append('P')
		elif c == 'ACT' or c == 'ACC' or c == 'ACA': aas.append('T')
		elif c == 'ACG':                             aas.append('T')
		elif c == 'GCT' or c == 'GCC' or c == 'GCA': aas.append('A')
		elif c == 'GCG':                             aas.append('A')
		elif c == 'TAT' or c == 'TAC':               aas.append('Y')
		elif c == 'TAA' or c == 'TAG' or c == 'TGA': aas.append('*')
		elif c == 'CAT' or c == 'CAC':               aas.append('H')
		elif c == 'CAA' or c == 'CAG':               aas.append('Q')
		elif c == 'AAT' or c == 'AAC':               aas.append('N')
		elif c == 'AAA' or c == 'AAG':               aas.append('K')
		elif c == 'GAT' or c == 'GAC':               aas.append('D')
		elif c == 'GAA' or c == 'GAG':               aas.append('E')
		elif c == 'TGT' or c == 'TGC':               aas.append('C')
		elif c == 'TGG':                             aas.append('W')
		elif c == 'CGT' or c == 'CGC' or c == 'CGA': aas.append('R')
		elif c == 'CGG':                             aas.append('R')
		elif c == 'AGA' or c == 'AGG':               aas.append('R')
		elif c == 'AGT' or c == 'AGC':               aas.append('S')
		elif c == 'GGT' or c == 'GGC' or c == 'GGA': aas.append('G')
		elif c == 'GGG':                             aas.append('G')
		else:                                        aas.append('X')
	return ''.join(aas)

def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)
	
def hydropathy(aa):
	if	 aa == 'A': return  1.80
	elif aa == 'C': return  2.50
	elif aa == 'D': return -3.50
	elif aa == 'E': return -3.50
	elif aa == 'F': return  2.80
	elif aa == 'G': return -0.40
	elif aa == 'H': return -3.20
	elif aa == 'I': return  4.50
	elif aa == 'K': return -3.90
	elif aa == 'L': return  3.80
	elif aa == 'M': return  1.90
	elif aa == 'N': return -3.50
	elif aa == 'P': return -1.60
	elif aa == 'Q': return -3.50
	elif aa == 'R': return -4.50
	elif aa == 'S': return -0.80
	elif aa == 'T': return -0.70
	elif aa == 'V': return  4.20
	elif aa == 'W': return -0.90
	elif aa == 'Y': return -1.30
	else:			return 'error: not an amino acid'

def oligotemp(seq):
	nts = {'AT': 0, 'GC': 0}
	for nt in seq:
		if nt == 'A' or nt == 'T': nts['AT'] += 1
		if nt == 'G' or nt == 'C': nts['GC'] += 1
	if len(seq) <= 13: tm = nts['AT']*2 + nts['GC']*4
	if len(seq) >  13: tm = 64.9 + 41*(nts['GC'] - 16.4)/len(seq)
	return tm