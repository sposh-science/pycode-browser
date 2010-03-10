from numpy import *
import pylab as p
import matplotlib.axes3d as p3

w = v = u = linspace(0, 4*pi, 100)

fig=p.figure()
ax = p3.Axes3D(fig)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.plot3D(u,v,sin(w))
ax.plot3D(u,sin(v),w)
ax.plot3D(sin(u),v,u)
p.show()
