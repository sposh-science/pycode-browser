from pylab import *
from scipy import *

def vj0(xarray):
	y = []
	for  x in xarray:
		val = special.j0(x)        # Compute Jo
		y.append(val)
	return y

a = linspace(0,10,100)
b = vj0(a)
plot(a,b)
show()
