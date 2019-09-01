import scipy
import pylab

a = scipy.poly1d([3,4,5])
print( a, ' is the polynomial')
print( a*a, 'is its square')
print( a.deriv(), ' is its derivative')
print( a.integ(), ' is its integral')
print( a(0.5), 'is its value at x = 0.5')

x = scipy.linspace(0,5,100)
b = a(x)
pylab.plot(x,b)
pylab.show()
