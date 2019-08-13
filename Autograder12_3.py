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

count = int(input("Enter count:"))
possition = int(input("Enter possition:"))

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Aisling.html"
print(url)
ilosc =0
while ilosc<count:
    ilosc = ilosc +1
    miejsce = 0
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    tags = soup.find_all('a')
    for tag in tags:
        miejsce = miejsce + 1
        if possition == miejsce:
            url = tag.get('href', None)
            print(url)
