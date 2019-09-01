# Plot Cv/NkB vs kBT/hw  
# The Einstein model of the solid predicts the heat capacity accurately at high temperatures,
# but noticeably deviates from experimental values at low temperatures.

import numpy as np
import pylab

T = np.linspace(0,2.,4000)  #  Create a temperature axis [0,2] with 4K equally spaced points
beta = 1./T  # Calculate the reciprocal (hw/kBT) . hw=1, kB=1
Cv = beta*beta*np.exp(beta)/((np.exp(beta)-1)**2)  # Calculate Cv

pylab.plot(T, Cv ,'-r') # Plot kBT/e vs Cv
pylab.xlabel('kB*T/hw'); pylab.ylabel('Cv= B^2*exp(beta)/(exp(beta)-1)^2')
pylab.show()
