#Example polyplot.py

from pylab import *
x = linspace(-pi, pi, 100)
a = poly1d([-1.0/5040,0,1.0/120,0,-1.0/6,0,1,0])
y = a(x)
plot(x,y)
show()
