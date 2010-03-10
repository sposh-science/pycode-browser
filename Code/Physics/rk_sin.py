from pylab import *

def func(t):
	return cos(t)

def rk4(s,t):
	k1 = dt * func(t)
	k2 = dt * func(t + dt/2.0)
	k3 = dt * func(t + dt/2.0)
	k4 = dt * func(t + dt)
	return s + ( k1/6 + k2/3 + k3/3 + k4/6 )

t = 0.0         # Stating angle
dt = 0.01       # value of angle increment   
val = 0.0        # value of the 'sine' function at t = 0

tm = [0.0]      # List to store theta values
res = [0.0]	# RK4 results

while t < 2*pi:
  val = rk4(val,t)	# get the new value
  t = t + dt
  tm.append(t)
  res.append(val)

plot(tm, res,'+')
plot(tm, sin(tm))	# compare with actual curve
show()
              