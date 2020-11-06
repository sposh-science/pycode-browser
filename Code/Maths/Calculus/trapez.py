from math import *

def sqr(a):
	return a**2

def trapez(f, a, b, n):
	h = (b-a) / n
	sum = f(a)
	for i in range (1,n):
		sum = sum + 2 * f(a + h * i)
	sum = sum + f(b)
	return 0.5 * h * sum

print( trapez(sin,0.,pi,100))
print( trapez(sqr,0.,2.,100))
print( trapez(sqr,0,2,100))   # Why the error ?

