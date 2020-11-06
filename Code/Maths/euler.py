import math

h = 0.01    # stepsize
x = 0.0     # initail values
y = 0.0

while x < math.pi:
     print( x, y, math.sin(x)   )
     y = y + h * math.cos(x)   # Euler method
     x = x + h

