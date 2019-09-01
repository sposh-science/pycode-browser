'''
Solving initial value problem using 4th order Runge-Kutta method.
derivative depends on the value of the function.
f(x,y) = 1 + y**2
'''

from pylab import *

def f1(x,y):
       return 1 + y**2

def f2(x,y):
        return (y-x)/(y+x)

def rk4(x, y, fxy, h):   # x, y , f(x,y)
	k1 = h * fxy(x, y)
	k2 = h * fxy(x + h/2.0, y+k1/2)
	k3 = h * fxy(x + h/2.0, y+k2/2)
	k4 = h * fxy(x + h, y+k3)
	ny = y + ( k1/6 + k2/3 + k3/3 + k4/6 )
	#print( x,y,k1,k2,k3,k4, ny)
	return ny


h = 0.2   # stepsize
x = 0.0   # initail values
y = 0.0
print( rk4(x,y,f1,h) )

h = 1    # stepsize
x = 0.0    # initail values
y = 1.0
print( rk4(x,y,f2,h) )

