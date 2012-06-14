from pylab import *

x = []
y = []

f = open('xy.dat', 'r')
while True:
    s = f.readline()
    if len(s) < 3:
       break
    ss = s.split()
    print ss
    x.append(ss[0])
    y.append(ss[1])

plot(x,y)
show()

