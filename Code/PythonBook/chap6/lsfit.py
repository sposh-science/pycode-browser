from pylab import *

NP = 50
r = 2*ranf([NP]) - 0.5
x = linspace(0,10,NP)
data = 3 * x + 2 + r

xbar = mean(x)
ybar = mean(data)
b = sum(data*(x-xbar)) / sum(x*(x-xbar))
a = ybar - xbar * b
print( a,b)

y = a + b * x
plot(x,y)
plot(x,data,'ob')
show()

