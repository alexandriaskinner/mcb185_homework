#Authors: Alexandria Skinner

import sys
import math

probs = []
total = 0
entropy = 0
for arg in sys.argv[1:]:
	prob = float(arg)
	assert 0 < prob <= 1
	total += prob
	entropy -= prob * math.log2(prob)
assert math.isclose(total, 1)
print(entropy)