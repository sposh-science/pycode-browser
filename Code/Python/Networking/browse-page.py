import urllib
fhand = urllib.urlopen('http://localhost/test.html')
for line in fhand:
   print line.strip()

