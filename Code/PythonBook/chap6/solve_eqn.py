from numpy import *
b = array([0,9,0])
A = array([ [4,1,-2], [2,-3,3],[-6,-2,1]])
print( dot(linalg.inv(A),b))
