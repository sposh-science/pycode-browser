from pylab import *
from scipy import *

x = linspace(-pi,pi,40)
a = zeros(40)

plot(x,sin(x))
for n in  range(1,5):
	sign = (-1)**(n+1)
	term = x**(2*n-1) / factorial(2*n-1)
	a = a + sign * term
	print( n,sign)
	plot(x,term)
plot(x,a,'+')
show()
