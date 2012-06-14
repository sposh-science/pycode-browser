#Example npsin.py

from pylab import *
x = linspace(-pi, pi , 200)
y = sin(x)
y1 = sin(x*x)
plot(x,y)
plot(x,y1,'r')    
show()
