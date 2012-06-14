from numpy import *

p = poly1d([1,1,1,0])
dp = p.deriv()
dp2 = dp.deriv()
dp3 = dp2.deriv()

a = 0  # The known point
x = 0
while x < .5:
	tay = p(a) + (x-a)* dp(a) + \
         (x-a)**2 * dp2(a) / 2 + (x-a)**3 * dp3(a)/6
	print '%5.1f  %8.5f\t%8.5f'%(x, p(x), tay)
	x = x + .1

