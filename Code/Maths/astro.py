#Example astro.py

from pylab import *
a = 2
x = linspace(0,a,100)
y = ( a**(2.0/3) - x**(2.0/3) )**(3.0/2)
plot(x,y)
show()
