#cp_em.py -- Motion of charged particle in E & M fields
from numpy import *
import pylab as p
import matplotlib.axes3d as p3

Ex = 0.0	# Components of Applied Electric Field
Ey = 0.0
Ez = 2.0
Bx = 0.0	# Magnetic field
By = 0.0
Bz = 2.0

m = 2.0		# Mass of the particle
q = 5.0		# Charge

x = 0.0		# Components of initial position and velocity 
y = 0.0
z = 0.0
vx = 20.0
vy = 0.0
vz = 0.0

a = []
b = []
c = []

t = 0.0
dt = 0.01

while t < 6: 	# trace until time reaches 6 units
  Fx = q * (Ex + (vy * Bz) - (vz * By) )
  vx = vx + Fx/m * dt		# Acceleration = F/m; dv = a.dt
  Fy = q * (Ey - (vx * Bz) + (vz * Bx) )
  vy = vy + Fy/m * dt
  Fz = q * (Ez + (vx * By) - (vy * Bx) )
  vz = vz + Fz/m * dt
#  print vx,vy, sqrt(vx**2+vy**2)
  x = x + vx * dt
  y = y + vy * dt
  z = z + vz * dt
  a.append(x)
  b.append(y)
  c.append(z)
  t = t + dt
  
fig=p.figure()
ax = p3.Axes3D(fig)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.plot3D(a,b,c)
p.show()
