import string
def get_number():
   while 1:
      try:
         a = raw_input('Enter a number ')
         x = string.atof(a)
         return x
      except:
         print 'Enter a valid number'

print get_number()
