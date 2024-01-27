#25entropy.py by Alexandria Skinner

import math
def entropy(A, T, G, C):
	t  = A+T+G+C		#total number of nt
	
	if A == 0: Ha=0	
	else:	   Ha = (A/t) * math.log2(A/t)
	
	if T == 0: Ht=0
	else:	   Ht = (T/t) * math.log2(T/t)
	
	if G == 0: Hg=0
	else:	   Hg = (G/t) * math.log2(G/t)
	
	if C == 0: Hc=0
	else:	   Hc = (C/t) * math.log2(C/t)
	
	return -(Ha + Ht + Hg + Hc)
	
print(entropy(12, 32, 17, 20))
print(entropy(56, 23, 64, 39))
print(entropy(10, 99, 25, 17))
print(entropy(15, 0, 20, 0))