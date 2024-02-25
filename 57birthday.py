#Author: Alexandria Skinner

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
success = 0

for i in range(trials):
	calendar = []
	for i in range(days): calendar.append(0)

	for i in range(people):
		bday = random.randint(1, days)
		calendar[bday-1] += 1
	for i in range(days):
		if calendar[i] > 1:
			success += 1
			break
		else: continue
print(success/trials)