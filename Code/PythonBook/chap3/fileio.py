#Example fileio.py

from numpy import *
a = arange(10)
print( a)
a.tofile('myfile.dat')
b = fromfile('myfile.dat', dtype='int')
print( b)
