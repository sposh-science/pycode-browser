#Example rfile2.py

f = open('test.dat' , 'r')
print( f.read(7))      # get first seven characters
print( f.read())       # get the remaining ones
f.close()
