from numpy import *
from enthought.mayavi import mlab

polar = linspace(0,pi,100)
azimuth = linspace(0, 2*pi,100)
phi,th = meshgrid(polar, azimuth)

r = 0.25 * sqrt(5.0/pi) * (3 * cos(phi) ** 2 - 1) #Ylm(0,2)

x = r*sin(phi)*cos(th)
y = r*cos(phi)
z = r*sin(phi)*sin(th)
mlab.mesh(x, y, z)

mlab.show()

