# In Class Practice

import sys
import random

"""
Variables for determining genome coverage pattern
- length of read
- chromosome length
- number of reads

Similar to birthday problem
"""

csize = int(sys.argv[1]) #chromosome length
rsize = int(sys.argv[2]) #read length
rnum  = int(sys.argv[3]) #number of reads

#create empty chromosome
chr = []
for i in range(csize):
	chr.append(0)
	
#create random reads
for i in range(rnum):
	pos = random.randint(0,csize - rsize)
	for j in range(rsize):
		chr[pos + j] += 1
print(chr)

#min coverage (want to exclude ends)
min = rnum
for n in chr[rsize:-rsize]:
	if n < min: min = n
print(min)

#Window across values
seq = 'AGCTAATCGGTACCA'
k = 3
print(seq)
for i in range(0, len(seq) - k +1):
	print(seq[i:i+k])
	
#Translation (move over three each time)- same except ,3
#you can hard code three since translation always changes by 3
seq = 'AGCTAATCGGTACCA'
k = 3
print(seq)
for i in range(0, len(seq) - k +1, 3):
	print(seq[i:i+k])
	
#simple skewer problem
seq = 'AGCTAATCGGTACCA'
k = 8
print(seq)
for i in range(0, len(seq) - k +1, 1):
	win = seq[i:i+k]
	g = win.count('G')
	c = win.count('C')
	print(i, win, (g+c)/k)