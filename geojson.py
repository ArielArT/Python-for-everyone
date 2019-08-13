import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    #print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    #print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    #print('lat', lat, 'lng', lng)
    try:
        if js['results'][0]['address_components'][0]['types'][0] == 'locality':
            if js['results'][0]['address_components'][1]['types'][0] == 'administrative_area_level_1':
                location = js['results'][0]['address_components'][2]['short_name']
            else:
                location = js['results'][0]['address_components'][3]['short_name']
            print(location)
        elif js['results'][0]['address_components'][0]['types'][0] == 'neighborhood':
            location = js['results'][0]['address_components'][4]['short_name']
            print(location)
        else:
            location = js['results'][0]['address_components'][0]['types'][1]
            print("This is in a country terytory, but a ", location)
    except:
        print("jakas bzdura wpisana")

    print(js)


