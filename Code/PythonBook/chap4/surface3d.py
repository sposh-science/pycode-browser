from pylab import *
from mpl_toolkits.mplot3d import Axes3D
ax = Axes3D(figure())

x = arange(-3*pi, 3*pi, 0.1)
y = arange(-3*pi, 3*pi, 0.1)
xx, yy = meshgrid(x, y)
z = sin(xx) + sin(yy) 

ax.plot_surface(xx, yy, z, cmap=cm.jet, cstride=1)
#imshow(z)
show()

