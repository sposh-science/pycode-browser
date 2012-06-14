#Example polyplot.py

from pylab import *
x = linspace(0.5,2.5, 100)
y = 1 + sin(x)

plot(x,y,linewidth=2)

a = [1,1]
b = [0,1+sin(1.)]
plot(a,b,'b-',linewidth=2)

a = [2,2]
b = [0,1+sin(2.0)]
plot(a,b,'b-',linewidth=2)

xc = 1+.05
while xc < 2:
	a = [xc,xc]
	b = [0,1+sin(xc)]
	plot(a,b,'b-',linewidth=1)
	xc= xc + .1

xlim(0.,3)
ylim(0.,3)
show()
