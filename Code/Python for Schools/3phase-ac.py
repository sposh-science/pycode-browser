# Three phase AC waveforms, voltage between two phases

from pylab import *
t = linspace(0, .05, 300)  # 300 point array, from 0 to .1 seconds
f = 50        # 50 Hz AC
Vm = 230 * sqrt(2)
y1 = Vm * sin(2*pi*f*t) 	# phase 1
y2 = Vm * sin(2*pi*f*t + 120*pi/180) # phase 2, 120 degree out of phase
y3 = Vm * sin(2*pi*f*t + 240*pi/180) # phase 3, 120 degree out of phase

plot(t, y1)		
plot(t, y2)		
plot(t, y3)		
plot(t, y2-y1, color='black')		
show()
