import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:

    address='http://py4e-data.dr-chuck.net/comments_209751.xml'
    uh = urllib.request.urlopen(address, context=ctx)
    print('Enter location:',address)

    data = uh.read()
    print('Retrieving',address)
    print('Retrieved', len(data), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data)
    #print(tree)
    suma = 0
    liczba =0
    counts = tree.findall('.//count')
    for count in counts:
        suma = suma + int(count.text)
        liczba = liczba + 1
    print('Count', liczba,'\nsum', suma, )
    break