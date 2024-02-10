#47deathsaves.py by Alexandria Skinner

import random

limit = 10000

deaths = 0
revivals = 0
stable = 0

for i in range(limit):
	fail = 0
	success = 0
	while True:
		roll = random.randint(1, 20)
		
		if roll == 1:
			fail += 2
			if fail >= 3:
				deaths += 1
				break
		elif 1 < roll < 10: 
			fail += 1
			if fail >= 3:
				deaths += 1
				break
		elif 10 <= roll < 20:
			success += 1
			if success == 3: 
				stable += 1
				break
		
		else:
			revivals += 1
			break

print(f'Prob of dying:\t\t{deaths / limit}')
print(f'Prob of stabilizing:\t{stable / limit}')
print(f'Prob of reviving:\t{revivals / limit}')
