def change(x):
  global counter  # use the global variable
  counter = x

counter = 10      
change(5)
print( counter)