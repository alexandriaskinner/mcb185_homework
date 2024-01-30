#21quadratic.py by Alexandria Skinner

def quad_formula(a, b, c):		#ax**2 + bx + c
	x1 = (-b + (b**2-4*a*c)**.5) / (2*a)
	x2 = (-b - (b**2-4*a*c)**.5) / (2*a)
	if (b**2-4*a*c) < 0: return 'no x-intercepts'
	else:				 return x1,x2
	
print(quad_formula(5, -8,  0))		#x=1.6, 0
print(quad_formula(1, -4, -10))		#x=5.74, -1.74
print(quad_formula(2,  4,  8))		#doesn't have x-intercepts