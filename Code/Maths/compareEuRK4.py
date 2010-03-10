'''
Sine function is calculated using its derivative, cosine.
Using Euler and RK4 method, with
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
y = 0.0     # for Euler
z = 0.0     # for RK4

while x < math.pi:
     print x, y - math.sin(x), z - math.sin(x) # errors   
     y = y + h * math.cos(x)       # Euler method
     z = rk4(x,z,math.cos,h)       # Runge-Kutta method
     x = x + h

