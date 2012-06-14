#Newton Raphson method

from pylab import *

def f(x):
	return 2.0 * x**2 - 3*x - 5

def df(x):
	return 4.0 * x - 3

vf = vectorize(f)
x = linspace(-2, 5, 100)
y = vf(x)

x1 = 4
tg1 = df(x1)*(x-x1) + f(x1)
x1 = -3
tg2 = df(x1)*(x-x1) + f(x1)

grid(True)
plot(x,y)
plot(x,tg1)
plot(x,tg2)
ylim([-20,40])
show()
