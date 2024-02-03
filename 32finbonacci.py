#32fibonacci.py by Alexandria Skinner

def fibonacci(limit):
	n1 = -1
	n2 = 1
	for i in range(limit):
		f = n1 + n2
		print(f)
		n1 = n2
		n2 = f

fibonacci(10)
