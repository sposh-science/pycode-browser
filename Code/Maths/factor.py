#Example factor.py

def factorial(n): # a recursive function
    if n == 0: 
         return 1 
    else: 
         return n * factorial(n-1) 
print factorial(10) 
