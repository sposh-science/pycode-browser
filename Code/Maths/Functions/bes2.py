from pylab import *
from scipy import *

def vjn(n,xarray):
	y = []
	for  x in xarray:
		val = special.jn(n,x)        # Compute Jn(x)
		y.append(val)
	return y

a = linspace(0,10,100)
for n in range(5):
	b = vjn(n,a)
	plot(a,b)
show()
