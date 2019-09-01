from pylab import *

mark = ['x','o','^','+','>']
NR = 2  # number of rows
NC = 3  # number of columns
pn = 1
for row in range(NR):
   for col in range(NC):
        subplot(NR, NC, pn) 
        a = rand(10) * pn
        plot(a, marker = mark[(pn+1)%5])
        xlabel('plot %d X'%pn)
        ylabel('plot %d Y'%pn)
        pn = pn + 1
show()
