"""
spring2.py 
The rk4_two() routine in this program does a two step integration using
an array method. The current x and xprime values are kept in a global 
list named 'val'. 
val[0] = current position; val[1] = current velocity
The results are compared with analytically calculated values.
"""

from pylab import *

def accn(t, val):	
	force = -spring_const * val[0] - damping * val[1]
	return force/mass
	
def vel(t, val):
	return val[1]

def rk4_two(t, h):	# Time and Step value
	global xxp	# x and xprime values in a 'xxp'
	k1 = [0,0]	# initialize 5 empty lists.
	k2 = [0,0]
	k3 = [0,0]
	k4 = [0,0]
	tmp= [0,0]	

	k1[0] = vel(t,xxp)
	k1[1] = accn(t,xxp)
	for i in range(2):	# value of functions at t + h/2
		tmp[i] = xxp[i] + k1[i] * h/2 

	k2[0] = vel(t + h/2, tmp)
	k2[1] = accn(t + h/2, tmp)
	for i in range(2):	# value of functions at t + h/2
		tmp[i] = xxp[i] + k2[i] * h/2 

	k3[0] = vel(t + h/2, tmp)
	k3[1] = accn(t + h/2, tmp)
	for i in range(2):	# value of functions at t + h
		tmp[i] = xxp[i] + k3[i] * h 

	k4[0] = vel(t+h, tmp)
	k4[1] = accn(t+h, tmp)

	for i in range(2):	# value of functions at t + h
		xxp[i] = xxp[i] + ( k1[i] + \
		2.0*k2[i] + 2.0*k3[i] + k4[i]) * h/ 6.0


t = 0.0         	# Stating time
h = 0.01      		# Runge-Kutta step size, time increment  
xxp = [2.0, 0.0]        # initial position & velocity
spring_const = 100.0    # spring constant
mass = 2.0         	# mass of the oscillating object
damping = 0.0

tm = [0.0]         	# Lists to store time, position & velocity
x = [xxp[0]]
xp = [xxp[1]]
xth = [xxp[0]]

while t < 5:
  rk4_two(t,h)			# Do one step RK integration
  t = t + h
  tm.append(t)
  xp.append(xxp[1])
  x.append(xxp[0])
  th = 2.0 * cos(sqrt(spring_const/mass)* (t))
  xth.append(th)

plot(tm,x)
plot(tm,xth,'+')
show()

