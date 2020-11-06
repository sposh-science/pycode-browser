#Solving initial value problem using 4th order Runge-Kutta method.
'''
Solving initial value problem using 4th order Runge-Kutta method.
Sine function is calculated using its derivative, cosine.
'''
import math

def rk4(x, y, yprime, dx = 0.01):   # x, y , derivative, stepsize
	k1 = dx * yprime(x)
	k2 = dx * yprime(x + dx/2.0)
	k3 = dx * yprime(x + dx/2.0)
	k4 = dx * yprime(x + dx)
	return y + ( k1/6 + k2/3 + k3/3 + k4/6 )


h = 0.01    # stepsize
x = 0.0     # initail values
y = 0.0

while x < math.pi:
     print( x, y, math.sin(x)   )
     y = rk4(x,y,math.cos)       # Runge-Kutta method
     x = x + h

