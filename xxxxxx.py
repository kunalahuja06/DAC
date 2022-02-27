# Latitude Longitude to PlusCode
import requests
import json
# parameters = {
#     'Authorization' : 'c10858b22145a1495827ced9348a6a35',
#     'address' : 'A-25 Teresa Triumph JB Nagar Andheri East ,Mumbai 400059'
# }
# response = requests.get("https://atlas.mapmyindia.com/api/places/geocode?", params=parameters)
# print(response)
# r = json.loads(response.text)
# # print(r['plus_code']['global_code'])

# response = requests.post('https://outpost.mapmyindia.com/api/security/oauth/token?grant_type=client_credentials&client_id=33OkryzDZsJDFvFHpxPOfyeNLmN0DjrE3vmv2mcHFwwSERFZ2qdsTEkJvsZzeK1HmAG0HtPGX5K2Wa1LYEEDWg==&client_secret=lrFxI-iSEg93VSa-41cUF1Y81i8O4czjRl7qr-HbngCO9cGwpKadJVasO91unIQ1y6o2_7EcZ0iLv1lNlttHLDVxPT4SVM-b')
# r = json.loads(response.text)
# print(r['access_token'])

# 359a0fa2-dada-4e92-a603-08226be37642

# import requests
endpoint = "https://atlas.mapmyindia.com/api/places/geocode?"
data = {"address": "jabalp"}
headers = {"Authorization": "Bearer 359a0fa2-dada-4e92-a603-08226be37642"}

print(requests.post(endpoint, headers=headers).json())
