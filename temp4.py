import requests
import json

parameters = {
    'address' : '18.54842,73.88788'
}
# GET https://plus.codes/api?address=14.917313,-23.511313  [PLUSCODE]


response = requests.get("https://plus.codes/api", params=parameters)
r = json.loads(response.text)
print(r['plus_code']['global_code'])
