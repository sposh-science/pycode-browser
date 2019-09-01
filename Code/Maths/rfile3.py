#Example rfile3.py

f = open('data.dat' , 'r')

while 1: # infinite loop
    s = f.readline()
    if s == '' :    # Empty string means end of file
         break      # terminate the loop
    m = int(s)      # Convert to integer
    print( m * 5     )
f.close()
