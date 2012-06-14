import math

#write some data to a file
f = open("/tmp/data.txt",'w')
for x in range(100):
    f.write(str(x))
    f.write(" ")
    f.write(str(x**3)+"\n")
f.close()
