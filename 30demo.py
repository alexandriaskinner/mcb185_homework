# 30demo.py by Alexandria Skinner

"""
while True:
	print ('hello')

i = 0
while True:
	i = i +1
	print('hey', i)
	if i == 3: break

i = 0
while i < 3:
	print(i)
	i = i +1
print('final value of i is', i)

i = 1
while i < 10:
	print(i)
	i = i +3
print('final value of i is', i)

#range functions
for i in range(1, 10, 3):
	print(i)
	
for i in range(0, 5):
	print(i)

for i in range(5): print(i)
for i in range(0, 5): print(i)
for i in range(0, 5, 1): print(i)

for char in 'hello':
	print(char)
	
seq = 'GAATTC'
for nt in seq:
	print(nt)
	
for i in range(len(seq)):
	print(seq[i])
	
for nt1 in 'ACGT':
	for nt2 in 'ACGT':
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')

nts = 'ACGT'
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')
		
limit = 4
for i in range(0, limit):
	for j in range(i + 1, limit):
		print(i+1, j+1)

def gc_comp(seq):
	gc_count = 0
	total    = 0
	for nt in seq:
		if nt == 'C' or nt == 'G':
			gc_count = gc_count +1
		total = total + 1
	return gc_count / total

print(gc_comp('ACAGCGAAT'))
"""
"""
#Practice Problems:
def triangular_number(n):
	#this function returns the sum of numbers 1 to n
	total = 0
	i = 0
	for i in range(n):
		i = i + 1
		total = total + i
	return total
print(triangular_number(4))
print(triangular_number(5))

def factorial(n):
	if n == 0: return 1
	total = 1
	i = 1
	for i in range(n):
		i = i + 1
		total = total * i
	return total
print(factorial(4))

def eulers_number(n):
	# n is the finite number of iterations for the function to complete
	e = 0
	i = 0
	for i in range(n):
		e = e + 1 / factorial(i)
	return e
print(eulers_number(100))


def perfect_square(n):
	#this function determines if a number is a perfect square
	root = math.sqrt(n)
	if root == root // 1: return True
	return False
print(perfect_square(9))

def prime(n):
	for i in range(2, n//2):
		if n % i == 0: return false
	return True


#In Class Notes:
def chksum(s):
	n = 0
	for c in s:
		n = n +ord(c)
	return n % 256

def maxchar(s):
	mx = 0
	for c in s:
		if ord(c) > mx:
			mx = ord(c)
	return mx

def minchar(s):
	mn = 255
	for c in s:
		if ord(c) < mn:
			mn = ord(c)
	return mn
name = 'alexandria'
print(chksum(name))
print(maxchar(name))
print(minchar(name))
"""

#loop inside loop
limit = 5
for i in range(1, limit):
	for j in range(i, limit): 
		#i = half matrix + major diagonal
		#1 instead of i = full matrix
		#i + 1 = half matrix - major diagonal
		print(i, j, 'c')
		
for i in range(1,limit):  #full matrix - major diagonal
	for j in range(1, limit):
		if i != j:
			print(i, j, 'c')