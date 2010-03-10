#Example vdiff.py

from pylab import *

def f(x):
        return sin(x)

def deriv(x,dx=0.005):
        df = f(x+dx/2)-f(x-dx/2)
        return df/dx

vecderiv = vectorize(deriv)

x = linspace(-2*pi, 2*pi, 200)
y = vecderiv(x)
plot(x,y,'+')
plot(x,cos(x))
show()
