# Plot Cv vs kBT/e  
# Def : phenomenon where the specific heat capacity of a solid at low temperature has a peak.
# It is called  anomalous because the heat capacity usually increases with temperature, or stays constant. 

import numpy as np
import pylab

T = np.linspace(0,4.,4000)  #  Create a temperature axis [0,4] with 4K equally spaced points
beta = 1./T  # Calculate the reciprocal (1/kBT) . kB=1
Cv = beta*beta*np.exp(beta)/((1+np.exp(beta))**2)  # Calculate Cv

pylab.plot(T, Cv ,'-r') # Plot kBT/e vs Cv
pylab.xlabel('T'); pylab.ylabel('Cv= B^2*exp(beta)/(1+exp(beta))^2')
pylab.show()
