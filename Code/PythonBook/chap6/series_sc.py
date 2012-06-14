from pylab import *

def factorial(n): # a recursive function
    if n == 0: 
         return 1 
    else: 
         return n * factorial(n-1) 

NP = 100
x = linspace(-pi, pi, NP)
sinx = zeros(NP)
cosx = zeros(NP)

for n in range(10):
        sinx += (-1)**(n) * (x**(2*n+1)) / factorial(2*n+1)
        cosx += (-1)**(n) * (x**(2*n))   / factorial(2*n)

plot(x, sinx)
plot(x, cosx, 'r')
show()
