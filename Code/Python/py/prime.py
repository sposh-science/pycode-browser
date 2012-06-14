def prime(x):
    y=x/2
    while (y>1):
        if x%y == 0:
            print x, 'has factor', y
            break
        y=y-1
    else:
        print x, # 'is prime'

if __name__=='__main__':
    for i in range(1,101):
        prime(i)
 		
