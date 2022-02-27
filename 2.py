from opencage.geocoder import OpenCageGeocode
from pprint import pprint

key = '14ea8113699f4d699547e947ad815b6b'
geocoder = OpenCageGeocode(key)

results = geocoder.reverse_geocode(44.8303087, -0.5761911)
print(results)

key = '14ea8113699f4d699547e947ad815b6b'
geocoder = OpenCageGeocode(key)

query = u'Bosutska ulica 10, Trnje, Zagreb, Croatia'
results = geocoder.geocode(query)
print('-------------------------')
print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'], 
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))
# 45.797095;15.982453;hr;Europe/Belgrade
