#Example ellipse.py

from pylab import *
a = 2
b = 3
t = linspace(0, 2 * pi, 100)
x = a * sin(t)       
y = b * cos(t)
plot(x,y)
show()
