# Validity of stirling's approximation
import math

def stirling(N):  #approximation function. log(n!)  = nlog(n)-n
    return N*math.log(N) - N
errors=[]
factN=1
print('N\tActual\tApprox\t%Error')
for N in range(1,110): # loop from N=1 to N=99
	factN *= N  # factorial is automatically calculated and revised per iteration.	
	actual = math.log(factN)
	approx = stirling(N)
	
	if(N>2): #Actual is 0 at N=1, and error is quite high for N=2 => neglect
		err = 100*(actual-approx)/actual
		errors.append(err)
		#Print values to the screen every 5 iterations
		if N%5==0:print ('%d\t%.2f\t%.2f\t%.2f'%(N,actual, approx, err))

#Plot N vs %error 
from pylab import *
# x = [3 ... 119] , y = errors
plot(range(3,110),errors)
xlabel('N');ylabel('percentage error')
show()
