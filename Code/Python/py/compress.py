import sys, bz2

if (len(sys.argv) < 2):
    sys.exit("Error!")

file = sys.argv[1]
fp = open(file, 'r')
data = fp.read()
comp = bz2.compress(data)
fp.close()
file = file + '.bz2'
fp = open(file, 'w')
fp.write(comp)
fp.close()
