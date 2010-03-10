#spring3d.py
from visual import *

base = box (pos=(0,-1,0), length=16, height=0.1, width=4, color=color.blue)
wall = box (pos=(0,0,0), length=0.1, height=2, width=4, color=color.white)
ball = sphere (pos=(4,0,0), radius=1, color=color.red)
spring = helix(pos=(0,0,0), axis=(4,0,0), radius=0.5, color=color.red)
ball2 = sphere (pos=(-4,0,0), radius=1, color=color.green)
spring2 = helix(pos=(0,0,0), axis=(-4,0,0), radius=0.5, color=color.green)

t = 0.0
dt = 0.01
x1 = 2.0
x2 = -2.0
v1 = 0.0
v2 = 0.0
k = 1000.0
m = 1.0

while 1:
  rate(20)

  f1 = -k * x1 
  v1 = v1 +  (f1/m ) * dt	# Acceleration = Force / mass ; dv = a.dt

  f2 = -k * x2 - v2		# damping proportional to velocity
  v2 = v2 +  (f2/m ) * dt	# Acceleration = Force / mass ; dv = a.dt
  
  x1 = x1 + v1 * dt
  x2 = x2 + v2 * dt
  t = t + dt
  
  spring.length =  4 + x1
  ball.x =  x1 + 4
  spring2.length = 4 - x2
  ball2.x =  x2 - 4
