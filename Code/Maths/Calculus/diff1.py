#Calculating and plotting derivatives
from pylab import *
dx = 0.1                # value of x increment
x = arange(0,10, dx)
y = sin(x)
yprime = []             # empty list
for k in range(99):     # from 100 points we get 99 diference values
        dy = y[k+1]-y[k]
        yprime.append(dy/dx)

x1 = x[:-1]       	# A new array without the last element
x1 = x1 + dx/2          # The derivative corresponds to the middle point
plot(x1, yprime, '+')
plot(x1, cos(x1))       # Cross check with the analitic value
show()
