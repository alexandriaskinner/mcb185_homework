#44randompi.py by Alexandria Skinner

import random

total = 0
inside = 0
while True:
	x = random.random()
	y = random.random()
	c = (x**2 + y**2)**0.5
	if c < 1: inside += 1
	total += 1
	pi = 4 * inside / total
	print(pi)