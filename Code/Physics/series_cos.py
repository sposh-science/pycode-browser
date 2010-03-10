import scipy, pylab

def mycos(x):
	res = 0.0
	for n in range(18):
		res = res + (-1)**n *	(x ** (2*n)) / scipy.factorial(2*n)
	return res

def vmycos(ax):
	y = []
	for x in ax:
		y.append(mycos(x))
	return y
	
x = scipy.linspace(0,4*scipy.pi,100)
y = vmycos(x)
pylab.plot(x,y)
pylab.plot(x,scipy.cos(x),'+')
pylab.show()
	
