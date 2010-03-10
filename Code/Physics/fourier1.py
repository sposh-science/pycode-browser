from pylab import * 
x = linspace(0.0, 2 * pi, 100)
y = sin(x)
for h in range(3,10,2):         # Add even harmonics to get square wave
        y = y + sin(h*x)/h
plot(x,y)
show()
