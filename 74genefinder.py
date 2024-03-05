#74genefinder.py by Alexandria Skinner

import sys
import mcb185

#seq =   'ATGATGGATGCGAATTAAGTAAGTCTGGGTTACAT'
#anti = 'ATG TAA CCC AGA CTT ACT TAA TTC GCA TCCATCAT'

minorf = 300

def find_cds(seq, min, strand):
	"""reports cds info, input= sequence, minimum length of protein in nt, plus or minus strand"""
	for frame in range(3):
		fseq = seq[frame:]
		i = 0
		while i < len(seq):
			codon = fseq[i:i+3]
			if codon == 'ATG':
				for j in range(i, len(seq)-2, 3): 
					codon = fseq[j:j+3]
					if codon == 'TGA' or codon == 'TAG' or codon =='TAA':
						if strand == '+':
							start = i + 1 + frame
							stop  = j + 3 + frame
						if strand == '-':
							stop = len(seq) - i - frame
							start  = len(seq) - j - 2 - frame
						if abs(j + 3 - i) > min:
							print(f'{id[0]}\tCDS\t{start}\t{stop}\t{strand}')
						i = j
						break
			i += 3

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	id = defline.split()
	print(find_cds(seq, minorf, '+'))
	print(find_cds(mcb185.anti_seq(seq), minorf, '-'))

"""
{id[0]}\t

def find_cds(seq, orflen):
	for frame in range(3):
		fseq = seq[frame:]
		stops_used = {}
		i = 0
		while i < len(seq):
			codon = fseq[i:i+3]
			if codon == 'ATG':
				for j in range (i, len(fseq) -2, 3):
					codon = fseq[j:j+3]
					if codon == 'TAA' or codon == 'TGA' or codon == 'TAG':
						stop = j
						if stop not in stops_used:
							return('gene', i+1, j+3)
							if j+2-i >= orflen: print(j+2-i)
							stops_used[stop] = True
		i += 3
"""
"""
turn into function because you have to do reverse separately

len(anti) - i - 1, len(anti) - j - 3

check data for positions in E. coli gene coordinates

defline(.split), RefSeq, CDS, smaller position, larger position, ., +/-, 0/., ID...
"""