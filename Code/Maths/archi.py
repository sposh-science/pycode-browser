#Example archi.py

from pylab import *
a = 2
th= linspace(0, 10*pi,200)
r = a*th
polar(th,r)
axis([0, 2*pi, 0, 70])
show()
