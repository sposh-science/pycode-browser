from pylab import *

def eval(a,xpoints,x):
    n = len(xpoints) - 1   
    p = a[n]
    for k in range(1,n+1):
        p = a[n-k] + (x -xpoints[n-k]) * p
    return p

def coef(x,y):
	a = copy(y)
	m = len(x)
	for k in range(1,m):
			a[k:m] = (a[k:m] - a[k-1])/(x[k:m]-x[k-1])
	return a

x  = array([0,1,2,3])
y  = array([0,3,14,39])
coef = coef(x,y)

NP = 20
newx = linspace(0,3, NP) # New x-values
newy = zeros(NP)
for i in range(NP):
	newy[i] = eval(coef, x, newx[i])
plot(newx, newy,'-x')
plot(x, y,'ro')
show()

