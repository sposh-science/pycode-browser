from numpy import *

def spf(x):
    return 3*x 

vspf = vectorize(spf)
a = array([1,2,3,4])
print( vspf(a))
