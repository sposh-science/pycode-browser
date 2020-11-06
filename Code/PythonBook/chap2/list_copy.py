a = [1,2,3,4]
print( a)
b = a
print( a == b)
b[0] = 5
print( a)

import copy
c = copy.copy(a)
c[1] = 100
print( a is c)
print( a, c)

