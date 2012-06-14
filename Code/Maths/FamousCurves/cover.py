from pylab import *

th = linspace(0, 10*pi,1000)
r = 4* sin(8*th)
polar(th,r)
r = sqrt(th)
polar(th,r)
polar(th, -r)
show()

