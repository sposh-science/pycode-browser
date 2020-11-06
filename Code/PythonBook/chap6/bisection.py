import math
def func(x):
        return x**3 - 10.0* x*x + 5

def bisect(f, x1, x2, epsilon=1.0e-9):
    f1 = f(x1)
    f2 = f(x2)
    if f1*f2 > 0.0: 
        print( 'x1 ans x2 are on the same side of x-axis')
        return None
    n = math.ceil(math.log(abs(x2 - x1)/epsilon)/math.log(2.0))
    n = int(n)
    for i in range(n):
        x3 = 0.5 * (x1 + x2)
        f3 = f(x3)
        if f3 == 0.0: return x3
        if f2*f3 < 0.0:
             x1 = x3
             f1 = f3
        else:
             x2 =x3
             f2 = f3
    return (x1 + x2)/2.0


print( bisect(func, 0.70, 0.8, 1.0e-4))
print( bisect(func, 0.70, 0.8, 1.0e-9))

