import requests
import json
import pprint
response = requests.get("https://randomuser.me/api")
if response.ok:
    data = response.json()
    user = data["results"][0]
    print(f"name:{user['name']['first']}")
    print(f"countri:{user['location']['country']}")
    print("-"*30)
    pprint.pprint(data)
    pprint.pprint(user)
else:
    print("oshibka, ti oshibsya")