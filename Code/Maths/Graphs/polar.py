#Example polar.py

from pylab import *
th = linspace(0,2*pi,100)
r = 5 * ones(100)  # radius = 5
axis([0, 2*pi, 0, 10])
polar(th,r)
show()
