#34scoringmatrix.py by Alexandria Skinner

nts = 'ACGT' 
print(end='   ')           #To align nts sequence with scores in following lines
for nt1 in nts:
	print(nt1, end='  ')
print()                    #To return to a new line
for nt1 in nts:
	print(nt1, end=' ')
	for nt2 in nts:
		if nt1 == nt2: print('+1', end=' ')
		else:          print('-1', end=' ')
	print()
