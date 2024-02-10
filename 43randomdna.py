#43randomdna.py by Alexandria Skinner

import random

limit = 3  #number of sequences you want
for seq in range(1, limit+1):
	print(f'>seq-{seq}')
	length = random.randint(50, 60)
	for nt in range(length):
		print(random.choice('AGCT'), end='')
	print()