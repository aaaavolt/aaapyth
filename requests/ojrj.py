import requests
URL = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url=URL)
print(response, "\n" )
print(response.status_code, "\n")
print(response.text, "\n")
resp_json = response.json()
print(resp_json, "\n")
print(
 
    f"""номнер шутки: {resp_json['id']}
    тип шутки:{resp_json['type']}
    шутка:{resp_json['setup']}
    {resp_json['punchline']}"""

)