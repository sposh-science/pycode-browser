from pylab import *
x = []                  # empty lists
y = []
for k in range(100):
        ang = 0.1 * k
        sang = sin(ang)
        x.append(ang)
        y.append(sang)
plot(x,y)
show()
