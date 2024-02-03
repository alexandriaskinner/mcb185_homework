#33triples.py by Alexandria Skinner

def integer_triples(limit):
	for a in range(1, limit+1):
		for b in range(a, limit+1):
			c = (a**2 + b**2)**0.5
			if c == c // 1: print(a, b, c)
			
print(integer_triples(100))
