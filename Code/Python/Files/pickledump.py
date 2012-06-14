#Example pickle.py

import pickle
f = open('test.pck' , 'w')
pickle.dump(12.3, f) # write a float type
f.close()
