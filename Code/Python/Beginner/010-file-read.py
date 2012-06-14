from pylab import *
#read from /tmp/data.txt
f = open('/tmp/data.txt','r')
x=[]
y=[]
for data in f:
    a,b=data.split(" ")
    x.append(int(a))
    y.append(int(b))
plot(x,y)
grid()
show()
