#Example circ.py

from pylab import *
a = 10.0
x = linspace(-a, a , 200)
yupper = sqrt(a**2 - x**2)
ylower = -sqrt(a**2 - x**2)
plot(x,yupper)
plot(x,ylower)
show()
