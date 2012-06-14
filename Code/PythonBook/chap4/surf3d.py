from numpy import *
from enthought.mayavi.mlab import *

x, y = mgrid[-10.:10.05:0.1, -10.:10.05:0.05]
z = sin(x) + sin(y)
surf(x, y, z)
show()
