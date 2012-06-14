#Example fourier_sawtooth.py

from pylab import * 
N = 100    # number of points
x = linspace(-pi, pi, N)
y = zeros(N)

for n in range(1,10): 
    term = (-1)**(n+1) * sin(n*x) / n
    y = y + term
plot(x,y)
show()
