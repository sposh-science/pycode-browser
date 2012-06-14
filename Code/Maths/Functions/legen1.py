from scipy import linspace, special
import pylab

x = linspace(-1,1,100)

for n in range(1,6):
	leg = special.legendre(n)
	y = leg(x)
	pylab.plot(x,y)
pylab.show()
