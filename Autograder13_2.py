import urllib.request, urllib.parse, urllib.error
import json
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    address='http://py4e-data.dr-chuck.net/comments_209752.json'
    uh = urllib.request.urlopen(address, context=ctx)
    print('Enter location:',address)

    data = uh.read().decode()
    print('Retrieving',address)
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = json.loads(data)
    #print(tree)
    suma = 0
    liczba =0

    for count in tree['comments']:
        wynik = count['count']
        suma = suma + wynik
        liczba = liczba + 1
    print('Count', liczba,'\nsum', suma, )
    break