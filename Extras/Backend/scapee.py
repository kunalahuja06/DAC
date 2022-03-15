
import requests
from bs4 import BeautifulSoup

Locations_file = 'Locations _to_lookup.xlsx'
Locations_Sheet = 'Sheet1'
Col_name = 'Locations'

locations_array = ['Mumbai']
features = ['Location', 'Latitude', 'Longitude']
Complete_df = []


https://www.google.com/search?q=Mumbai


for loc in locations_array:
    desired_location = loc
    # search_url = 'https://www.google.com/search?q='
    url = search_url + str(desired_location.replace(' ','+'))
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content)
    body = soup.find('body')
    map_class = body.find('a',{'class' :'qrSWbe KDZjCd'},  
                          href=lambda href: href and "maps" in href)
    map_url = map_class.get('href')
    r_map = requests.get(map_url)
    content_map = r_map.text
    soup_map = BeautifulSoup(content_map)
    head = soup_map.find('head')
    url_long_lat = head.find_all('meta')[8].get('content')
    Lat, Long = url_long_lat[url_long_lat.find('center=')+
                         len('center='):url_long_lat.rfind('&zoom')].split('%2C')
    location_info = pd.DataFrame([[desired_location,Lat,Long]])
    location_info.columns = features
    Complete_df = Complete_df.append(location_info, ignore_index = True)
    
print(Complete_df)