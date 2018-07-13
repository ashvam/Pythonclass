import beautifulsoup

import urllib.request
page = urllib.request.urlopen('https://www.bloomberg.com/quote/SPX:IND')
s = page.read()
print(s)