#Example circpar.py

from pylab import *
a = 10.0
th = linspace(0, 2*pi, 200)
x = a * cos(th)
y = a * sin(th)
plot(x,y)
show()
