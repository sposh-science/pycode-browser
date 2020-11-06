from numpy import *

def coef(x,y):
	a = copy(y)
	m = len(x)
	for k in range(1,m):
			a[k:m] = (a[k:m] - a[k-1])/(x[k:m]-x[k-1])
	return a

x  = array([0,1,2,3])
y  = array([0,3,14,39])
print( coef(x,y))

