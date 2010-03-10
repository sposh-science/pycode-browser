#spring1.py
from pylab import *
t = 0.0         # Stating time
dt = 0.01       # value of time increment
x = 10.0         # initial position
v = 0.0         # initial velocity
k = 10.0       # spring constant 
m = 2.0         # mass of the oscillating object

tm = []         # Empty lists to store time, velocity and displacement
vel = []
dis = []

while t < 5:
  f = -k * x                    # Try (-k*x - 0.5 * v) to add damping
  v = v +  (f/m ) * dt          # dv = a.dt 
  x = x + v * dt                # dS = v.dt 
  t = t + dt
  tm.append(t)
  vel.append(v)
  dis.append(x)

plot(tm,vel)
plot(tm,dis)
show()
