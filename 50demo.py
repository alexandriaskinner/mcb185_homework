#50demo.py by Alexandria Skinner
"""
seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq: print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])

#Slices
s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s[0:5], s[:5])
print(s[5:len(s)], s[5:])
print(s, s[::], s[::1], s[::-1])

#Tuples:
tax = ('Homo', 'sapiens', 9606)
print(tax[0])
print(tax[::-1])

def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2

x1, x2 = quadratic(5, 6, 1)
print(x1, x2)
intercepts = (quadratic(5, 6, 1))
print(intercepts[0], intercepts[1])

#enumerate() and zip()
nts = 'AGCT'
for i in range(len(nts)):
	print(i, nts[i])
for i, nt in enumerate(nts):
	print(i, nt)
	
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

#Lists:
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)
nts.append('C')
print(nts)
last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)

alph = 'ABCDEFGHIJKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

text = 'good day  to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

#Searching
if 'A' in alph: print('yay')
if 'a' in alph: print('no')
print('index G?', alph.index('G'))
#print('index Z?', alph.index('Z'))
print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

if thing in list: idx = list.index(thing)

#Practice
list1 = [12, 23, 11, 28]
def min(list):
	min = list[0]
	for n in list[1:]:
		if n < min: min = n
	return min
print(min(list1))

def min_max(list):
	min = list[0]
	max = list[0]
	for n in list[1:]:
		if n < min: min = n
		if n > max: max = n
	return max, min
print(min_max(list1))

def mean(list):
	total = 0
	sum = 0
	for n in list[0:]:
		total += 1
		sum += n
	return (sum/total)
print(mean(list1))
	
import math	
def entropy(distribution):
	sum = 0
	for prob in distribution[0:]:
		sum -= (prob * math.log2(prob))
	return sum
print(entropy([0.4, 0.1, 0.1, 0.4]))

def kldist(d1, d2):
	sum = 0
	for p, q in zip(d1, d2):
		sum += p * math.log2(p/q)
	return sum
distribution1 = [0.1, 0.1, 0.4, 0.4]
distribution2 = (0.25, 0.25, 0.25, 0.25)
print(kldist(distribution1, distribution2))

#Files
i = int('42')
x = float('0.61803')
"""
#In Class: Calculating the Median
import sys
print(sys.argv[1:]) #[1:] just numbers no file name, but they aren't numbers
#need int to convert

val = []
for x in sys.argv[1:]:
	val.append(int(x))
print(val)
val.sort()
print(val)

if len(val) % 2 == 0: 
	median = (val[len(val)//2] + val[len(val)//2 - 1]) / 2
else:
	median = val[len(val) // 2]           
print(median)