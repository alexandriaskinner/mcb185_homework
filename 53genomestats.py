#Authors: Alexandria Skinner

import gzip
import sys

gffpath = sys.argv[1]
feature = sys.argv[2]

count = 0
min = 100000
max = 0
total = 0
val = []
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		if line[0] != '#':
			word = line.split()
			if word[2] == feature:
				count += 1
				l = int(word[4]) - int(word[3]) + 1
				if l < min: min = l
				if l > max: max = l
				total += l
				val.append(l)
mean = total / count

sumdev = 0
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		if line[0] != '#':
			word = line.split()
			if word[2] == feature:
				l = int(word[4]) - int(word[3]) +1
				sumdev += (mean - l)**2
stdev = (sumdev / count)**0.5

val.sort()
if len(val) % 2 == 0:
	median = (val[len(val)//2] + val[len(val)//2 -1]) / 2
else:
	median = val[len(val) // 2]

print(f'N: {count}, min: {min}, max: {max}, mean: {mean:.0f}, stdev: {stdev:.0f}, med: {median:.0f}')