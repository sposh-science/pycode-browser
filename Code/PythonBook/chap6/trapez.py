from math import *

def sqr(a):
	return sqrt(1.0 - a**2)

def trapez(f, a, b, n):
	h = (b-a) / n
	sum = f(a)
	for i in range (1,n):
		sum = sum + 2 * f(a + h * i)
	sum = sum + f(b)
	return 0.5 * h * sum

print 4*trapez(sqr,0.,1.,100)
print 4*trapez(sqr,0.,1.,1000)
print 4*trapez(sqr,0,1,100)   # Why the error ?

