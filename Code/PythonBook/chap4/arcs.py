#Example arcs.py

from pylab import *
a = 10.0
for a in range(5,21,5):
    th = linspace(0, pi * a/10, 200)
    x = a * cos(th)
    y = a * sin(th)
    plot(x,y)
show()
