# Validity of stirling's approximation up to N=100 and plot N vs actual, N vs approx
import math

def stirling(N):  #approximation function. log(n!)  = nlog(n)-n
    return N*math.log(N) - N
ACTUAL=[]
APPROX=[]
factN=1
MAXNUM = 100
print('N\tActual\tApprox\t%Error')
for N in range(1,MAXNUM): # loop from N=1 to N=99
	factN *= N  # factorial is automatically calculated and revised per iteration.	
	actual = math.log(factN)
	approx = stirling(N)
	
	ACTUAL.append(actual)
	APPROX.append(approx)

	if(N>2): #Actual is 0 at N=1, and error is quite high for N=2 => neglect
		err = 100*(actual-approx)/actual
		#Print values to the screen every 5 iterations
		if N<5: print ('%d\t%.2f\t%.2f\t%.4f'%(N,actual, approx, err))
		elif N<100 and N%20==0: print ('%d\t%.2f\t%.2f\t%.4f'%(N,actual, approx, err))
		elif N%100==0:print ('%d\t%.2f\t%.2f\t%.4f'%(N,actual, approx, err))

#Plot N vs actual, and N vs approx 
from pylab import *
N = range(1,MAXNUM)
plot(N,APPROX,'-b', label = "N vs Approximation")
plot(N,ACTUAL,'-r', label = "N vs Actual")
legend(loc='lower right')

xlabel('Actual');ylabel('ln(N!) , NlnN-N')
show()
