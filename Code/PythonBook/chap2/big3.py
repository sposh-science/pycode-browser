x = 1
while x < 10:
   if x < 3:
       print 'skipping work', x
       x = x + 1
       continue
   print x
   if x == 4:
       print 'Enough of work'
       break
   x = x  + 1
print 'Done'

