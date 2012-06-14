#Example fermat.py

from pylab import *
a = 2
th= linspace(0, 10*pi,200)
r = sqrt(a**2 * th)
polar(th,r)
polar(th, -r)
show()
