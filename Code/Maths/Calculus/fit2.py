from pylab import *
from scipy import *
from scipy.optimize import leastsq

def  err_func(p,y,x):
	A,k,theta = p
	return y - A*sin(2*pi*k*x+theta)

def evaluate(x,p):
	return p[0] * sin(2*pi*p[1]*x+p[2])

ax = arange(0, 0.2, 0.001)
A,k,theta = 5, 50.0, pi/3
y_true = A*sin(2*pi*k*ax+theta)
y_meas = y_true + 0.2*randn(len(ax))

p0 = [6, 50.0, pi/3]
plsq = leastsq(err_func,p0,args=(y_meas,ax))
print plsq

plot(ax,y_true)
plot(ax,y_meas,'o')
plot(ax,evaluate(ax,plsq[0]))
show()
