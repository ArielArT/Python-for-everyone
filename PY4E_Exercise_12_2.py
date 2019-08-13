import socket


while (True):
    adres = input("Podaj stronke:")
    strona = adres.split("/")
    if strona[0] != "http:" : 
        print("zly host http:")
        continue   
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        mysock.connect((strona[2], 80))
        break
    except:
        print("nie mozna sie polaczyc z : ",adres)
        continue
    
komenda = 'GET '+adres+' HTTP/1.0\r\n\r\n'
cmd = komenda.encode()
mysock.send(cmd)

lenght = 0

print("\n\nPoczatek danych\n\n")
while True:
    data = mysock.recv(3000)
    lenght = lenght + len(data)
    if len(data) < 1:
        break
    if lenght < 3001 :
        print(data.decode(),end='')
        print("\n\ndlugosc danych",lenght)
print("\n\nKoniec danych\n\n")
print (lenght)
mysock.close()


#%% Exercise 12.3
"""
http://data.pr4e.org/mbox-short.txt
"""

# Search for lines that start with From and have an at sign
import urllib.request

fhand = urllib.request.urlopen('https://www.w3.org/Protocols/rfc2616/rfc2616.txt')

ilosc = 0
one = 0

for line in fhand:
    ilosc = ilosc + len(line.decode())

    if ilosc <= 3000:
        print(line.decode().strip())
    elif ilosc > 3000 and one == 0:
        koniec = 3000 - (ilosc - len(line.decode()))
        ostatnia = line[:koniec]
        print(ilosc)
        print(len(ostatnia))
        print(ostatnia.strip())
        one = 1

print("\n",ilosc)


#%% 12.4

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))


















