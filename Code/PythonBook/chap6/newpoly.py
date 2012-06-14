from copy import copy

def coef(x,y):
	a = copy(y)
	m = len(x)
	for k in range(1,m):
		tmp = copy(a)
		for i in range(k,m):
			tmp[i] = (a[i] - a[i-1])/(x[i]-x[i-k])
		a = copy(tmp)
	return a

x  = [0,1,2,3]
y  = [0,3,14,39]
print coef(x,y)


