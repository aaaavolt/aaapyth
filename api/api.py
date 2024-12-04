import requests
import json
import pprint
# response = requests.get("https://randomuser.me/api")
# if response.ok:
#     data = response.json()
#     user = data["results"][0]
#     print(f"name:{user['name']['first']}")
#     print(f"countri:{user['location']['country']}")
#     print("-"*30)
#     pprint.pprint(data)
#     pprint.pprint(user)
# else:

#     print("oshibka, ti oshibsya"
#------------------------------------------
# response = requests.get("https://api.quotable.io/random")

# if response.status_code == 200:
#     data = response.json()
#     print(data['content'," ", 'author'])
# else:
#     print("oshibka")
#--------------------------------------

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "hello, API",
    "body": "this is test post!",
    "userId":1
}
response = requests.post(url,json=data)
if response.status_code == 201:
    print("+")
    print(response.json())
else:
    print("-")