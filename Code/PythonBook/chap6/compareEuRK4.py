'''
Cosine function is integrated by Euler and RK4 methods. 
Results at each step is compared with sine function.
'''
from pylab import *



def rk4(x, y, fx, h = 0.1):   # x, y , derivative, stepsize
	k1 = h * fx(x)
	k2 = h * fx(x + h/2.0)
	k3 = h * fx(x + h/2.0)
	k4 = h * fx(x + h)
	return y + ( k1/6 + k2/3 + k3/3 + k4/6 )

h = 0.1     # stepsize
x = 0.0     # initail values
ye = 0.0    # for Euler
yr = 0.0    # for RK4
ax = []     # Lists to store calculated values
euerr = []
rkerr = []

while x < 2*pi:
     ye = ye + h * math.cos(x)       # Euler method
     yr = rk4(x, yr, cos, h)    # Runge-Kutta method
     x = x + h  
     ax.append(x)
     euerr.append(ye - sin(x))
     rkerr.append(yr - sin(x))
  
plot(ax,euerr,'+')
plot(ax, rkerr,'ro')
show()

