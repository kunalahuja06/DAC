import h3
lat, lng = 36.22552316, -88.296323236
print(lat,lng,"Latlong")
resolution = 9
x = h3.geo_to_h3(lat, lng, resolution)
print("HEX ",x)

y = h3.h3_to_geo(x)
print("GeoCoordinates ",y)


# import requests
# import json

# parameters = {
#     "key" : "z67NlpBAN5F49cWUaXBVjUjB8dHvScP0",
#     "location" : "Eiffel Tower" #19.1089507,72.8646233,
# }

# response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
# r = json.loads(response.text)
# li = r['results'][0]['locations'][0]['latLng']

# t1 = (li['lat'],li['lng'])
# print(t1)
