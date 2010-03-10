#Example: max.py

max = 0

while 1:        # Infinite loop
   x = input('Enter a number ')
   if x > max:
      max = x
   if x == 0:
      print max
      break
