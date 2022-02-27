import requests
import json

parameters = {
    "key" : "z67NlpBAN5F49cWUaXBVjUjB8dHvScP0",
    "location" : "Teresa Triumph Society" #19.1089507,72.8646233,
}

response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
r = json.loads(response.text)
li = r['results'][0]['locations'][0]['latLng']

print(li['lat'],li['lng'])

# 19.1089063,72.8631741

# GET https://plus.codes/api?address=14.917313,-23.511313  [PLUSCODE]

# 7JCJWRQP+G3