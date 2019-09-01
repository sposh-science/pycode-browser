'''
Region of a complex plane ranging from -1 to +1 in both real
and imaginary axes is rpresented using a 2 dimensional matrix
having X x Y elements.For X and Y equal to 200, the stepsize
in the complex plane is 2.0/200 = 0.01.
The nature of the pattern depends very much on the value of c.
'''

from pylab import *
X = 200
Y = 200
rlim = 1.0
ilim = 1.0
rscale = 2*rlim / X
iscale = 2*ilim / Y
MAXIT = 100
MAXABS = 2.0

c = 0.02 - 0.8j   # The constant in equation z**2 + c

m = zeros([X,Y],dtype=uint8)  # A two dimensional array

def numit(x,y):       # number of iterations to diverge
     z = complex(x,y)
     for k in range(MAXIT):
            if abs(z) <= MAXABS:
                 z = z**2 + c         
            else:
                 return k     # diverged after k trials
     return MAXIT            # did not diverge,

for x in range(X):
    for y in range(Y):
         re = rscale * x - rlim  # complex number represented
         im = iscale * y - ilim  # by the (x,y) coordinate
         m[x][y] = numit(re,im)  # get the color for (x,y)

imshow(m)  # Colored plot using the two dimensional matrix
show()

