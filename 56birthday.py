#Author: Alexandria Skinner

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

success = 0
for i in range(trials):
	bdays = []
	for j in range(people):
		bday = random.randint(0, days)
		bdays.append(bday)
	samebday = 0
	for k in bdays[1:]:
		for l in bdays[k+1:]:
			if k == l:
				samebday += 1
	if samebday >= 1: success += 1
	
print(success / trials)