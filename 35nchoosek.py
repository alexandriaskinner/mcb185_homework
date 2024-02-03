#35nchoosek.py by Alexandria Skinner

def factorial(n):
	if n == 0: return 1
	total = 1
	i = 1
	for i in range(n):
		i = i + 1
		total = total * i
	return total
	
def nchoosek(n, k):
	return factorial(n) / (factorial(k) * factorial(n-k))

print(nchoosek(3, 2))
print(nchoosek(10, 8))
print(nchoosek(13, 19))