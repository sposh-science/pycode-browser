#Example: format2.py

a = 'justify as you like'
print( '%30s'%a)
print( '%-30s'%a)       # minus sign for left justification
for k in range(1,11):   # A good looking table
    print( '5 x %2d = %2d' %(k, k*5))
