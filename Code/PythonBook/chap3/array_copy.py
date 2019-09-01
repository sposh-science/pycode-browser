from numpy import *
a = zeros(3)
print( a)
b = a
c = a.copy()
c[0] = 10
print( a, c)
b[0] = 10
print( a,c)
