#37nilakantha.py by Alexandria Skinner

def pi(limit):
	x  = 2
	pi = 3
	for i in range(limit):
		term = 4 / (x * (x+1) * (x+2))
		pi = pi + (-1)**(i) * term
		x = x + 2
	return pi

print(pi(1))
print(pi(2))
print(pi(3))
print(pi(100))