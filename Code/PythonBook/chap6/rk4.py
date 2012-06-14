'''
Solving initial value problem using 4th order Runge-Kutta method.
Sine function is calculated by integrating its derivative, cosine.
'''
from pylab import *

def rk4(x, y, fx, h = 0.01):   # x, y , derivative, stepsize
	k1 = h * fx(x)
	k2 = h * fx(x + h/2.0)
	k3 = h * fx(x + h/2.0)
	k4 = h * fx(x + h)
	return y + ( k1/6 + k2/3 + k3/3 + k4/6 )



h = 0.01    # stepsize
x = 0.0     # initail values
y = 0.0
ax = [x]
ay = [y]
while x < math.pi:
     y = rk4(x,y,math.cos)       # Runge-Kutta method
     x = x + h
     ax.append(x)
     ay.append(y)
plot(ax,ay)
show()
