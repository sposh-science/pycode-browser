#Example series_sin.py

from pylab import *
from scipy import factorial

x = linspace(-pi, pi, 50)
y = zeros(50)
for n in range(5):
        term = (-1)**(n) * (x**(2*n+1)) / factorial(2*n+1)
        y = y + term
        plot(x,term)

plot(x, y, '+b')
plot(x, sin(x),'xr') # compare with the real one
show()
