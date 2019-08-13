# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:14:06 2019
http  port = 80 
https port = 443
@author: Zakochani
"""

# dla Python 3.7 w konsoli
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl, re

count = 0
suma = 0
liczba = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_209749.html"
html = urlopen(url).read()

soup = BeautifulSoup(html, 'lxml')
sciezka = r'\d+'
# Retrieve all of the anchor tags
tags = soup.find_all('span')
for tag in tags:
    # Look at the parts of a tag
    dopasowanie = re.search(sciezka,str(tag))
    if dopasowanie:
        liczba= float(dopasowanie.group())
        suma = liczba + suma
        count = count +1
    dopasowanie = None

print("Count",count,"\nSum",suma)
