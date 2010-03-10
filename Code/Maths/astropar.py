#Example astropar.py

from pylab import *
a = 2
t = linspace(-2*a,2*a,101)
x = a * cos(t)**3
y = a * sin(t)**3
plot(x,y)
show()
