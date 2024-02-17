#Authors: Alexandria Skinner
"""
split with tabs to get RGB
then split with , to get R or G or B
Compare color to file
kinda like finding the minimum value/difference 
between color and colornames file
"""
import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

rgbval = [R, G, B]
closest = 768  #max possible distance between two colors
with open(colorfile) as fp:
	for line in fp:
		values = []
		word = line.split('\t')	
		val = word[2].split(',')
	
		values.append(int(val[0]))
		values.append(int(val[1]))
		values.append(int(val[2]))
		
		dist = dtc(values, rgbval)
		if dist < closest:
			closest = dist
			closecolor = word[0]
print(closecolor)