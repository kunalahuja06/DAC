import requests

response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyDWAv5AAZCInsz8CONpkpP4KwU4VC8JX2w')
print(response)
resp_json_payload = response.json()
print(resp_json_payload)
# print(resp_json_payload['results'][0]['geometry']['location'])