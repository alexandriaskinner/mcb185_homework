#22oligotemp.py by Alexandria Skinner

def oligotemp(a, t, g, c):
	l= a+t+g+c									#length of sequence
	if l <= 13: T= (a+t)*2 + (g+c)*4			#Short sequences
	if l >  13: T= 64.9 + 41*(g+c-16.4)/l		#Longer sequences
	return T 

print(oligotemp(1, 3, 5, 2))
print(oligotemp(7, 11, 3, 9))
print(oligotemp(3, 6, 2, 2))