import urllib
import re
html = urllib.urlopen('http://localhost/test.html').read()
links = re.findall('href="(http://.*?)"', html)
for link in links:
    print link
