#Example fourier_square.py

from pylab import * 
N = 100    # number of points
x = linspace(0.0, 2 * pi, N)
y = zeros(N)
for n in range(5): 
    term = sin((2*n+1)*x) / (2*n+1)
    y = y + term
    plot(x,y)
show()
