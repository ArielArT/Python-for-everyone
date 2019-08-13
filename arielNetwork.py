

from bs4 import BeautifulSoup
import urllib


adres = "https://www.pythonforbeginners.com"

content = urllib.urlopen(adres).read()

soup = bs4.BeautifulSoup(content)

print(soup.prettify())

print(title)

print(soup.title.string)


print(soup.p)

