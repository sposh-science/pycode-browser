from pylab import *
from mpl_toolkits.mplot3d import Axes3D
ax = Axes3D(figure())

phi = linspace(0, 2 * pi, 100)
theta = linspace(0, pi, 100)

x = 10 * outer(cos(phi), sin(theta))
y = 10 * outer(sin(phi), sin(theta))
z = 10 * outer(ones(size(phi)), cos(theta))

ax.plot_wireframe(x,y,z, rstride=2, cstride=2)

show()

