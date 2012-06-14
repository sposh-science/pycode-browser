from scipy import *
from scipy import special
import pylab

def jn(n,x):
	jn = 0.0
	for k in range(30):
		num = (-1)**k * (x/2)**(2*k)
		den = factorial(k)*factorial(n+k)
		jn = jn + num/den
	return jn * (x/2)**n

def vjn_local(n,xarray):
	y = []
	for  x in xarray:
		val = jn(n,x)        # Jn(x) using our function
		y.append(val)
	return y
	
def vjn(n,xarray):
	y = []
	for  x in xarray:
		val = special.jn(n,x)        # Compute Jn(x)
		y.append(val)
	return y

a = linspace(0,10,100)
for n in range(2):
	b = vjn(n,a)
	c = vjn_local(n,a)
	pylab.plot(a,b)
	pylab.plot(a,c,marker = '+')
pylab.show()
