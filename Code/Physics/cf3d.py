import math
from visual import *

base = box (pos=(0,-5,0), length=15, height=0.01, width=0.01, color=color.black)
m1 = sphere (pos=(0,0,0), radius=1.0, color=color.blue)
m2 = sphere (pos=(4,0,0), radius=0.3, color=color.red)

G = -1.0
M = 1000.0
m = 1.0
dt = 0.01

x = math.sqrt(12.5)
y = x
vx = 10.0
vy = -vx+2

a = []
b = []
while 1:
  rate(50)
  r = sqrt(x**2 + y**2)
  v = sqrt(vx**2 + vy**2)
  F = G*M*m/r**2 + 0.7 * v
  Fx = F * x/r
  Fy = F * y/r

  vx = vx + Fx/m * dt
  vy = vy + Fy/m * dt
  x = x + vx * dt
  y = y + vy * dt
  m2.pos=(x,y,0)
  a.append(x)
  b.append(y)
  
