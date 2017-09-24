#Calculating the inverse of a matrix

from numpy import *
a = array([ [4,1,-2], [2,-3,3], [-6,-2,1] ], dtype='float')
ainv = linalg.inv(a)
print (ainv)
print (dot(a,ainv))
