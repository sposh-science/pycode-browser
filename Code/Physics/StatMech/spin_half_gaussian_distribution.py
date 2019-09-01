# Plot sigma(M,N) vs M/u  

import numpy as np
import pylab

M = np.linspace(-50,50.,4000)  #  Create a magnetic moment axis [-50,50] with 4K equally spaced points. u=1, so M/u = M
N = 100 # number of spins
sigma = np.exp(-1*(1./(2*N))*(M**2))

pylab.plot(M,sigma ,'-r') # Plot kBT/e vs Cv
pylab.xlabel('M/u'); pylab.ylabel('Sigma= e^(-1*(1./(2*N))*(M**2))')
pylab.show()
