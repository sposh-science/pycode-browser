#Example poly.py

from pylab import *
a = poly1d([3,4,5])
b = poly1d([6,7])
c = a * b + 5
d = c/a

print a
print a(0.5)
print b
print a * b
print a.deriv()
print a.integ()
print d[0], d[1]

