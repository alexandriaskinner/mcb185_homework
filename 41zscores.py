#41zscores.py by Alexandria Skinner

import random

z1 = 0
z2 = 0
z3 = 0
l = 100000
for i in range (l):
	n = random.gauss(0.0, 1.0)
	if n > 1: z1 += 1
	if n > 2: z2 += 1
	if n > 3: z3 += 1
print(1 - 2*z1/l, 1 - 2*z2/l, 1- 2*z3/l)
	