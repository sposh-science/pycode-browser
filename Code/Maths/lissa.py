#Example lissa.py

from pylab import *
a = 2
b = 3
t= linspace(0, 2*pi,100)
x = a * sin(2*t)       
y = b * cos(t)
plot(x,y)

x = a * sin(3*t)
y = b * cos(2*t)
plot(x,y)
show()
