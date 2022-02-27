
# # # Raw Address to Latitude/Longitude

# from opencage.geocoder import OpenCageGeocode

# key = '14ea8113699f4d699547e947ad815b6b'
# geocoder = OpenCageGeocode(key)

# address = 'A-25, Teresa triumph, JB Nagar, Andheri East, Mumbai 400059'
# query = address
# results = geocoder.geocode(query)
# latitude = results[0]['geometry']['lat']
# longitude = results[0]['geometry']['lng']

# print(latitude,longitude)

# results = geocoder.reverse_geocode(latitude, longitude)
# print(results[0]['geometry'])

# # 5-Ramwadi, Devidayal road, Mulund (w), Mumbai-400080 - 19.176 72.9522 - 89608b553b3ffff
# # eiffel tower coordinates - 48.8582602 2.2944991 - 891fb46741bffff
# # A-25, Teresa triumph, JB Nagar, Andheri East, Mumbai 400059 - 19.0111 73.8747 - 89608a8e56bffff




# # Latitude Longitude to H3 Code (h3 code is just like pluscode)
# import h3
# lat, lng = 19.0111,73.8747
# print(lat,lng,"Latlong")
# resolution = 9
# x = h3.geo_to_h3(lat, lng, resolution)
# print("HEX ",x)

# y = h3.h3_to_geo(x)
# print("GeoCoordinates ",y)




# Latitude Longitude to PlusCode
import requests
import json
parameters = {
    'address' : '19.108914019118583, 72.86535472954193'
}
response = requests.get("https://plus.codes/api", params=parameters)
r = json.loads(response.text)
print(r['plus_code']['global_code'])
