import requests
response = requests.get("https://api.gihub.com")
print(response.json())