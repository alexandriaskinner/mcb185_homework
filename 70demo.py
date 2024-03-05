#70demo.py by Alexandria Skinner
"""
d = {'dog': 'woof', 'cat': 'meow'}

print(d)
print(d['cat'])

d['pig'] = 'oink'
print(d)

d['cat'] = 'mew'
print(d)

del d['cat']
print(d)

#print(d['rat'])
if 'dog' in d: print(d['dog'])

#Iteration:
for key in d: print(f'{key} says {d[key]}')
for k, v in d.items(): print(k, 'says', v)
for thing in d.items(): print(thing[0], thing[1]) #you shouldn't do it this way

print(d.keys(), d.values(), list(d.values()))

#Composition, again
seq = 'AGCTCCATGTAGCN'
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1
print(count)
"""
import itertools
for nts in itertools.product('ACGT', repeat=2):
	print(nts)

#In Class Notes:
size = 10000
#words = []
wordd = {}
for i in range(size): #Create dictionary of words
	token = []
	for j in range(10):
		token.append(random.choice('ABC'))
	token = ''.join(token)
	wordd[token] = True

for i in range(1000): #search for words
	if 'MYNAME' in wordd:
		print('founc')

#Dictionary is faster than going down a list
#Most of the time is spent setting up the dictionary
	#which is only done once