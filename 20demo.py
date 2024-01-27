# 20demo.py by Alexandria Skinner

print ('hello again') # greeting

"""
multi-line 
comment
"""

import math

print (1/2)
print (32/10)
print (32%10)
print (8**(2/3))
print (abs(-10))
print (pow(10, 2))
print (math.sqrt(4))
print (math.log(math.e))

a = 3
b = 4
c = math.sqrt(a**2 +b**2)
print (c)
print(type(a), type(b), type(c), sep=',')

def pythagoras(a,b):
	c = math.sqrt(a**2 +b**2)
	return c
x=pythagoras(3,4)
print(x)

def pythagoras2(a,b):
	if a <= 0: sys.exit('error: a must be greater than 0')
	if b <= 0: sys.exit('error: b must be greater than 0')
	return math.sqrt(a**2 +b**2)
print(pythagoras2(3,4))
print(pythagoras2(1,1))
print(pythagoras2(-1,1))


# Practice:
import math 
def changesign(a):
	return -1*a
print(changesign(3))

def sphere_vol(r):
	return 4*math.pi*(r**3)/3
print(sphere_vol (3))

def f_to_c(f):
	return (f-32)*5/9
print(f_to_c(32))

def mps_to_kph(s):
	return s*1.60934
print(mps_to_kph(65))

def DNAconc(OD260, dilution_factor):
	return 50*OD260*dilution_factor/(10**3)  #in mg/mL
print(DNAconc(0.70,50))
	
def midpt(x1, y1, x2, y2):
	xm= (x1+x2)/2
	ym= (y1+y2)/2
	return (xm,ym)
print(midpt(2,3,4,6))


#Strings, Conditionals, etc.
s = 'hello world'
print(s, type(s))

a = 2
b = 2
if a == b:
	print('a equals b')
print(a,b, sep=',')

c = a == b
print (c)
print (type(c))

if a < b:
	print('a < b')
elif a > b:
	print('a > b')
else:
	print('a == b')
	
if   a < b: print('a < b')
elif a > b: print('a > b')
else: 		print('a == b')

if a < b or a > b:  print('all things being equal, a and b are not')
if a < b and a > b: print('you are living in a strange world')
if not False: print(True)

a = 0.3
b = 0.1 * 3
if   a < b: print('a < b')
elif a > b: print('a > b')
else:		print('a ==b')

print(abs(a - b)) # 5.551115123125783e-17
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

s1='A'
s2='B'
s3='a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

a = 1
s = 'G'
if a < s: print('a < s')


#More Practice
def is_integer(x):
	y = x % 1
	if math.isclose(y,0): print('integer')
	else: 				  sys.exit('not an integer')
is_integer(4)

def is_odd(x):
	y = abs(x % 2)
	if math.isclose(y,1):	return 'odd'
	elif math.isclose(y,0): return 'even'
	else:					sys.exit('error: not an integer')
is_odd(-4)

def valid_prob(P):
	if 0 <= P <= 1: return 'valid probability'
	else:			return 'not a valid probability'
print(valid_prob(.5))

def nt_weight(nt):
	if   nt == 'T': print(304.2)   #in Daltons for all nt
	elif nt == 'A': print(313.21)
	elif nt == 'C': print(289.18)
	elif nt == 'G': print(329.21)
	else: sys.exit('error: not a base')
nt_weight('A')

def nt_pair(nt):
	if   nt == 'T': print('A')
	elif nt == 'A': print('T')
	elif nt == 'C': print('G')
	elif nt == 'G': print('C')
	else:			sys.exit('error: not a base')
nt_pair('A')
