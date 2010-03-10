from pylab import *
from numpy import *

x = linspace(0.0, 2 * pi, 100)
s = sin(x)      # sine of each element of 'x' is taken
c = cos(x)      # cosine of each element of 'x' is taken
plot(x,s)
plot(x,c)
show()   
