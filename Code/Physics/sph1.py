from pylab import *
from scipy import special

a_th = []	# list to store polar angle theta from -90 to + 90 deg
a_sph = []	# list to store absolute values if sperical harminics
phi = 0.0	# Fix azimuth, phi at zero

theta = -pi/2    	# start theta from -90 deg
while theta < pi/2:
	h = special.sph_harm(0,10, phi, theta)	# (m, l , phi, theta)
	a_sph.append(abs(h))
	a_th.append(theta * 180/pi)
	theta = theta + 0.02
plot(a_th,a_sph)
show()
