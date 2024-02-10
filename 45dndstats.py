#45dndstats.py by Alexandria Skinner

import random

trials = 10000

#3D6:
sum_stat = 0
total = 0
for i in range (trials):
	stat = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
	sum_stat += stat
	total += 1
	ave3d6 = sum_stat / total
print(f'3D6:\t{ave3d6}')

#3D6r1:
sum_stat = 0
total = 0
for i in range(trials):
	stat = random.randint(2, 6) + random.randint(2, 6) + random.randint(2, 6)
	sum_stat += stat
	total += 1
	ave3d6r1 = sum_stat / total
print(f'3D6r1:\t{ave3d6r1}')

#3D6x2:
sum_stat = 0
total = 0
for i in range(3*trials):
	d1 = random.randint(1,6)
	d2 = random.randint(1,6)
	if d1 > d2: roll = d1
	else:       roll = d2
	sum_stat += roll
	total += (1/3)
	ave3d6x2 = sum_stat / total
print(f'3D6x2:\t{ave3d6x2}')

#4D6d1:
sum_stat = 0
total = 0
for i in range(trials):
	d1 = random.randint(1,6)
	d2 = random.randint(1,6)
	d3 = random.randint(1,6)
	d4 = random.randint(1,6)
	if   d1 <= d2 and d1 <= d3 and d1 <= d4: stat = d2 + d3 + d4
	elif d2 <= d1 and d2 <= d3 and d2 <= d4: stat = d1 + d3 + d4
	elif d3 <= d1 and d3 <= d2 and d3 <= d4: stat = d1 + d2 + d4
	else:                                    stat = d1 + d2 + d3
	sum_stat += stat
	total += 1
	ave4d6d1 = sum_stat / total
print(f'4D6d1:\t{ave4d6d1}')