from opencage.geocoder import OpenCageGeocode

key = '14ea8113699f4d699547e947ad815b6b'
geocoder = OpenCageGeocode(key)

address = 'A-25, Teresa Triumph,Andheri, JB Nagar, Mumbai, India'
query = address
results = geocoder.geocode(query)
latitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng']

print(latitude,longitude)

results = geocoder.reverse_geocode(latitude, longitude)
print(results[0]['geometry'])


# [{'annotations': {'DMS': {'lat': "45° 47' 48.95736'' N", 'lng': "15° 58' 54.81948'' E"}, 'MGRS': '33TWL7630771954', 'Maidenhead': 'JN75xt71tg', 'Mercator': {'x': 1779096.332, 'y': 5717223.035}, 'OSM': {'edit_url': 'https://www.openstreetmap.org/edit?way=398295928#map=17/45.79693/15.98189', 'note_url': 'https://www.openstreetmap.org/note/new#map=17/45.79693/15.98189&layers=N', 'url': 'https://www.openstreetmap.org/?mlat=45.79693&mlon=15.98189#map=17/45.79693/15.98189'}, 'UN_M49': {'regions': {'EUROPE': '150', 'HR': '191', 'SOUTHERN_EUROPE': '039', 'WORLD': '001'}, 'statistical_groupings': ['MEDC']}, 'callingcode': 385, 'currency': {'alternate_symbols': [], 'decimal_mark': ',', 'format': '%n %u', 'html_entity': '', 'iso_code': 'HRK', 'iso_numeric': '191', 'name': 'Croatian Kuna', 'smallest_denomination': 1, 'subunit': 'Lipa', 'subunit_to_unit': 100, 'symbol': 'kn', 'symbol_first': 0, 'thousands_separator': '.'}, 'flag': '🇭🇷', 'geohash': 'u2 25ke9jdmph05hhvc576', 'qibla': 133.39, 'roadinfo': {'drive_on': 'right', 'road': 'Bosutska ulica', 'speed_in': 'km/h'}, 'sun': {'rise': {'apparent': 1645940400, 'astronomical': 1645934460, 'civil': 1645938600, 'nautical': 1645936500}, 'set': {'apparent': 1645979940, 'astronomical': 1645985820, 'civil': 1645981740, 'nautical': 1645983780}}, 'timezone': {'name': 'Europe/Belgrade', 'now_in_dst': 0, 'offset_sec': 3600, 'offset_string': '+0100', 'short_name': 'CET'}, 'what3words': {'words': 'notebook.libraries.provider'}}, 'bounds': {'northeast': {'lat': 45.7969724, 'lng': 15.9819653}, 'southwest': {'lat': 45.7968324, 'lng': 15.9818309}}, 'components': {'ISO_3166-1_alpha-2': 'HR', 'ISO_3166-1_alpha-3': 'HRV', '_category': 'building', '_type': 'building', 'city': 'Zagreb', 'continent': 'Europe', 'country': 'Croatia', 'country_code': 'hr', 'county': 'City of Zagreb', 'house_number': '10', 'neighbourhood': 'Mjesni odbor Trnje', 'political_union': 'European Union', 'postcode': '10000', 'road': 'Bosutska ulica', 'suburb': 'Gradska četvrt Trnje'}, 'confidence': 10, 'formatted': 'Bosutska ulica 10, 10000 Zagreb, Croatia', 'geometry': {'lat': 45.7969326, 'lng': 15.9818943}}]