#31fizzbuzz.py by Alexandria Skinner

limit = 100
for i in range(1, limit + 1):
	if   i % 15 == 0: print('FizzBuzz')
	elif i % 3  == 0: print('Fizz')
	elif i % 5  == 0: print('Buzz')
	else:             print(i)	