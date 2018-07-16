import urllib.request

from bs4 import BeautifulSoup

symbol = input("name your stock:")

ticker =  'https://www.nasdaq.com/symbol/'+ symbol
print(ticker)

page = urllib.request.urlopen(ticker)
s = page.read()

soup = BeautifulSoup(s, 'html.parser')
import csv
p = soup.find("div", {"id": "qwidget_lastsale"})
print(p.get_text())
csv = open('/Users/****/Desktop/stocklists.csv', 'a') #add the system path
csv.write(symbol)
csv.write(p.get_text())
csv.close()

#1
#with open('/Users/****/Desktop/stocklists.csv', 'wb') as file:
 #   for line in text
#print (soup.prettify())
# print(soup)
# print(list(soup.title))
#print(list(soup.p))
#print(list(soup.a))
#print(soup.h3)
#Lead-2-QuoteHeader-Proxy
#print(id('Lead-2-QuoteHeader-Proxy'))
#print(soup.find_all('h3'))