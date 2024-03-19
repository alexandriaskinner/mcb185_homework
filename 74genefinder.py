#74genefinder.py by Alexandria Skinner

import sys
import mcb185

minorf = sys.argv[2]

def find_cds(seq, min, strand):
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
						if abs(j + 3 - i) >= int(min):
							print(f'{id[0]}\tRefSeq\tgene\t{start}\t{stop}\t{strand}')
						i = j
						break
			i += 3

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	id = defline.split()
	print(find_cds(seq, minorf, '+'))
	print(find_cds(mcb185.anti_seq(seq), minorf, '-'))