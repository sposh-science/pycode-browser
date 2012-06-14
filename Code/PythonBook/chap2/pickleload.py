#Example pickle2.py

import pickle
f = open('test.pck' , 'r')
x = pickle.load(f)
print x , type(x)        # check the type of data read
f.close()
