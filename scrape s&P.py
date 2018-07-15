import urllib.request
import csv
from bs4 import BeautifulSoup

symbol = input("name your stock:")
ticker =  'https://www.nasdaq.com/symbol/'+ symbol
print(ticker)
with open('egg.csv', 'wb') as f
page = urllib.request.urlopen(ticker)
s = page.read()

soup = BeautifulSoup(s, 'html.parser')
#print (soup.prettify())
# print(soup)
# print(list(soup.title))
#print(list(soup.p))
#print(list(soup.a))
#print(soup.h3)
#Lead-2-QuoteHeader-Proxy
#print(id('Lead-2-QuoteHeader-Proxy'))
#print(soup.find_all('h3'))
p = soup.find("div", {"id": "qwidget_lastsale"})
print(p.get_text())