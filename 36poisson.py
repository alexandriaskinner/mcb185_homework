#36poisson.py by Alexandria Skinner

import math
def poisson_prob(n, k):
	return (n**k) * (math.e**(-n)) / math.factorial(k)

print(poisson_prob(10, 5))
print(poisson_prob(35, 60))