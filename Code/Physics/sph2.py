from numpy import *
from scipy import special
import pylab as p
import matplotlib.axes3d as p3

phi = linspace(0, 2*pi, 50)
theta = linspace(-pi/2, pi/2, 200)

ax = []
ay = []
az = []
R = 1.0
for t in theta:
	polar = float(t)
	for k in phi:
		azim = float(k)
		sph = special.sph_harm(0,2,azim, polar) # Y(m,l,phi,theta)
		modulation = 0.2 * abs(sph)
		r = R * ( 1 + modulation)
		x = r*cos(polar)*cos(azim)
		y = r*cos(polar)*sin(azim)
		z = r*sin(polar)
#		print z
#		print x,y,z
		ax.append(x)
		ay.append(y)
		az.append(z)
fig=p.figure()
f = p3.Axes3D(fig)
f.set_xlabel('X')
f.set_ylabel('Y')
f.set_zlabel('Z')
f.scatter3D(ax,ay,az)
p.show()
