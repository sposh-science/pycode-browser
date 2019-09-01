from math import *

def f1(x):
        return x**2
def f2(x):
        return x**4
def f3(x):
        return x**10
 
def deriv(func, x, dx=0.1):
        df = func(x+dx/2)-func(x-dx/2)
        return df/dx

print( deriv(f1, 1.0), deriv(f1, 1.0, 0.01) )
print( deriv(f2, 1.0), deriv(f2, 1.0, 0.01) )
print( deriv(f3, 1.0), deriv(f3, 1.0, 0.01))

 

