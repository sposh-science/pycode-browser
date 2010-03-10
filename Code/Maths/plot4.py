#Example plot4.py

from pylab import *
t = arange(0.0, 5.0, 0.2)
plot(t, t**2,'x')      # t^{2}
plot(t, t**3,'ro')     # t^{3}
show()
