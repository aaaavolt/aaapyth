# import requests
# URL = "https://official-joke-api.appspot.com/random_joke"

# response = requests.get(url=URL)
# print(response, "\n" )
# print(response.status_code, "\n")
# print(response.text, "\n")
# resp_json = response.json()
# print(resp_json, "\n")
# print(
 
#     f"""номнер шутки: {resp_json['id']}
#     тип шутки:{resp_json['type']}
#     шутка:{resp_json['setup']}
#     {resp_json['punchline']}"""

# )
def get_type(url):
    response = requests.get(url+"types")
    resp_json = response.json()
    for i in range(len(resp_json)):
        print(f"{i}: {resp_json[i]}")
    ans = int(input())
    return resp_json[ans]
def get_joke_by_type(url, type):
    response = requests.get(f"{url}jokes/{type}/random")
    resp_json = response.json()
    print(f"""
ceтап: {resp_json[0]['setup']}
панчлайн:  {resp_json[0]['punchline']}
""")
import requests
URL = "https://official-joke-api.appspot.com/"
ans = ""
while ans != "-":
    type = get_type(URL)
    get_joke_by_type(URL,type)
    ans = input("- to leave")

    

