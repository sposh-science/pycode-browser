#Example wfile2.py

f = open('data.dat' , 'w')
for k in range(1,4):
      s = '%3d\n' %(k)
      f.write(s) 
f.close()
