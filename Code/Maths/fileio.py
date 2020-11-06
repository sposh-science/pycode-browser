#Example fileio.py

from numpy import *
a = arange(10)
a.tofile('myfile.dat')
b = fromfile('myfile.dat')
print( b)
