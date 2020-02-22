def fib(n):
	a ,b, t = 0, 1, ''
	while a < n:
		t += str(a) + ' '
		a, b=b, a+b
	return t	
	print()
print(fib(10000))	