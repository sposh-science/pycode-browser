from pylab import *
x = linspace(0.0, 2 * pi, 100)
plot(sin(x), cos(x), 'b')       # plot lissagous figures
plot(sin(2*x), cos(x),'r')
plot(sin(x), cos(2*x),'y')
show()
