import math
def func(x):
	return x**3 - 10.0* x*x + 5

def rootsearch(f,a,b,dx):
    x = a
    while True:
	f1 = f(x)
	f2 = f(x+dx)
	if f1*f2 < 0:
		return x, x + dx
	x = x + dx
	if x >=  b: 
		print 'Failed to find root'
		return

x,y = rootsearch(func, 0.0,1.0,.1)
print x,y
x,y = rootsearch(math.cos, 0.0, 4,.1)
print x,y
