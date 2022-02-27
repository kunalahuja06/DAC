# from opencage.geocoder import OpenCageGeocode

# key = '14ea8113699f4d699547e947ad815b6b'
# geocoder = OpenCageGeocode(key)

# address = 'A-25, Teresa Triumph,Andheri, JB Nagar, Mumbai, India'
# query = address
# results = geocoder.geocode(query).0
# latitude = results[0]['geometry']['lat']
# longitude = results[0]['geometry']['lng']

# print(latitude,longitude)

# results = geocoder.reverse_geocode(latitude, longitude)
# print(results[0]['geometry'])



import h3
lat, lng = 36.22552316, -88.296323236
print(lat,lng,"Latlong")
resolution = 9
x = h3.geo_to_h3(lat, lng, resolution)
print("HEX ",x)

y = h3.h3_to_geo(x)
print("GeoCoordinates ",y)

