#integrate cosine using Euler method. The result should be sine
from pylab import *

h = 0.01    # stepsize
x = 0.0     # initail values
y = 0.0

ax = []
ay = []

while x < 2*pi:
     y = y + h * math.cos(x)   # Euler method
     x = x + h
     ax.append(x)
     ay.append(y)
plot(ax,ay)
show()
   
