from tkplot_class import *
from math import *

w = Tk()
gw1 = disp(w)
xy = []
for k in range(200):
	x = 2 * pi * k/200
	y = sin(x)
	xy.append((x,y))
gw1.setWorld(0, -1.0, 2*pi, 1.0)
gw1.line(xy)

gw2 = disp(w)
gw2.line([(10,10),(100,100),(350,50)], 'red')
w.mainloop()



