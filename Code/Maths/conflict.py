#Example conflict.py

from numpy import *
x = linspace(0, 5, 10) # make a 10 element array
print( sin(x))         # sin of scipy can handle arrays

from math import *     # sin of math will be called now
print( sin(x) )        # will give ERROR
