# http://scitation.aip.org/content/aapt/journal/ajp/83/10/10.1119/1.4923249
# Asymmetric wave functions from tiny perturbations
'''
Abstract:
The quantum mechanical behavior of a particle in a double well defies
our intuition based on classical reasoning. Not surprisingly, an asymmetry
in the double well will restore results more consistent with the 
classical picture. What is surprising, however, is how a very small asymmetry
can lead to essentially classical behavior. In this paper, we use the simplest 
version of a double-well potential to demonstrate these statements. 
We also show how this system accurately maps onto a two-state system,
which we refer to as a 'toy model.

License: GPL-V3
Author-email; jithinbp@gmail.com
'''

from scipy import linalg,integrate
import numpy as np
import time
from pylab import *
import pyperclip
def lazycopy(A):
	np.savetxt('tmp.csv',A)
	fo = open('tmp.csv', 'r').read()
	pyperclip.copy(fo)


########## PARAMETERS

spatial_scaling = 1.#0.52917725
a = 1.  # width of the infinite 1D potential
b = .2   #width of the barrier
N = 200  #the number of terms in the basis fn expansion
q = 5   #the number of wavefns to be plotted
a = a/spatial_scaling
b = b/spatial_scaling

E10 = np.pi*np.pi/2./a  #4.9348022 #(pi^2)/(2*a^2)
print( ('E10 = ',E10))
energy_scaling = 1./E10  #27.211396
V0 = 500 #depth of the well
V0= V0/energy_scaling

n = 5000

x = np.linspace(0,a,n)
V = V0*np.zeros(n);
b1= int(n*(a/2 - b/2)/a )
b2= int(n*(a/2 + b/2)/a )
V[b1:b2]=V0;

h=np.zeros([N,N]); #initialising the h matrix
areasR = []
areasL = []

######## PREPARE PLOTS

########Plot ground state + potential's shape
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()

ax1.set_xlabel('x/a')
ax1.set_ylabel('psi^2', color='g')
ax2.set_ylabel('V', color='b')

ax2.plot(x*spatial_scaling,V*energy_scaling, 'b-')


ax2.set_ylim([0,V0*energy_scaling+10])
#plt.title(lbl)


############# asymmetry  ###########

#delta = np.linspace(0,0.05,6)
delta = [0,2e-7,5e-7,1e-6,2e-6,1e-5]#np.linspace(0,0.05,6)
for VL in delta:
	V[0:b1]= -1*VL/energy_scaling
	
	#Determing the elements of the h matrix
	for i in range(N):
		for j in range(i,N):
			bi = np.sqrt(2/a)*np.sin(x*np.float((i+1)*np.pi/a));
			bj = np.sqrt(2/a)*np.sin(x*np.float((j+1)*np.pi/a));
			f = bi*V*bj;
			h[j,i] = integrate.simps(f,x);
			if (j==i):
				h[j,i] = h[j,i]+((j+1)**2)*(np.pi**2)*(0.5/a**2);
			h[i,j]=h[j,i];

	evals,evecs = linalg.eig(h)
	sortorder = evals.argsort()
	E = evals[sortorder]
	E=E*energy_scaling;
	evecs=evecs[:,sortorder]    #Corresonding eigen vectors
	#lazycopy(np.diagonal(h,1))

	psi = np.zeros([N,len(x)])
	for j in range(1): #We only need the ground state for now
		for m in range(N):
			psi[j,:]=psi[j,:]+evecs[m,j]*np.sqrt(2/a)*np.sin((m+1)*np.pi*x/a) #wavefn using eigen expansion


	PY = psi[0,:]**2 # +E[0]
	lbl = 'VL = -%.2e'%(VL)
	print( min(V),E[0],E[1],max(PY[:len(PY)/2]),max(PY[len(PY)/2:]))
	if VL==0:
		ax1.plot(x[::10]*spatial_scaling,PY[::10],color='R',label='symmetric wells')
	else:
		ax1.plot(x[::10]*spatial_scaling,PY[::10],color='G',label=lbl)
	areasL.append(np.trapz(PY[:len(PY)/2],dx = (x[1]-x[0]) ))
	areasR.append(np.trapz(PY[len(PY)/2:],dx = (x[1]-x[0]) ))
	
legend = ax1.legend(loc='upper right', shadow=True)
# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('0.90')

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize('small')

figure()
xlabel('perturbation(VR-VL)')
ylabel('Area under the curve')

plot(delta,areasL,color='R',label='Left well area')
plot(delta,areasR,color='G',label='Right well area')
show()

