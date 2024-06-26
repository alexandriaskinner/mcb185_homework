# 40demo.py by Alexandria Skinner
"""
import random
for i in range(5):
	print(random.random())

for i in range(50):
	print(random.choice('AGCT'), end='')
print()

for i in range(50):
	r = random.random()
	if r < 0.7: print(random.choice('AT'), end='')
	else:       print(random.choice('GC'), end='')
print()

for i in range(3):
	print(random.randint(1,6))

for i in range(5):
	print(random.gauss(0.0, 1.0))

#Pretty Printing
print('this line\nhas some\nline breaks')
print('a\tb\tcat\tdogma')
print(10, 20, 30, sep='\t')
print(100, 2000, 30000, 400000, sep='\t')

i = 1
pi = 3.14159
print('normal string {i} {pi}')
print(f'formatted string {i} {pi}')
print(f'tau {pi +pi}')

print(f'formatted string {i} {pi:.3f}')
"""

import sys
print('logging', file=sys.stderr)

#Monte Carlo
import random
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())