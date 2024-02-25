#Author: Alexandria Skinner and Amina Muhic

import mcb185
import sys

file = sys.argv[1]
w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(file):
	windinit = seq[0:w]
	c = windinit.count('C')
	g = windinit.count('G')
	comp = (g + c) / w
	if g + c == 0: skew = 0
	else:          skew = (g - c) / (g + c)
	print(f'0\t{comp:.3f}\t{skew:.3f}')
	
	for i in range(1, len(seq) -w +1):
		sold = seq[i-1]
		snew = seq[i+w-1]
		if sold == 'C': c -= 1 
		if sold == 'G': g -= 1
		if snew == 'C': c += 1
		if snew == 'G': g += 1
		
		comp = (g + c) / w
		if c + g == 0: skew = 0
		else:          skew = (g - c) / (g + c)
		print(f'{i}\t{comp:.3f}\t{skew:.3f}')
	
"""
Comparison between 61 and 62 at w = 1000 nt
-61skew.py: 21.06s
-62skew.py:  6.75s
"""
	
	