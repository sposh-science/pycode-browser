from pylab import *

def f(x):
	return 2.0 * x**2 - 3*x - 5

def df(x):
	return 4.0 * x - 3

def nr(x, tol = 1.0e-9):
	for i in range(30):
		dx = -f(x)/df(x)
		#print x
		x = x + dx
		if abs(dx) < tol: 
			return x

print nr(4)
print nr(1)
print nr(-4)
