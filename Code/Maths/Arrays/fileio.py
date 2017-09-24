#File R/W example

from numpy import *
a = arange(10)
a.tofile('myfile.dat')
b = fromfile('myfile.dat')
print (b)
