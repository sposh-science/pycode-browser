#Example diff.py

def f(x):
        return x**3

def deriv(x,dx=0.005):
        df = f(x+dx/2)-f(x-dx/2)
        return df/dx

print deriv(2.0)
print deriv(2.0, 0.1)
print deriv(2.0, 0.0001)
