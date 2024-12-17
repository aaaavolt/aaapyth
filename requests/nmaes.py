import requests
def get_all_by_name():
    name = input()
    params = {"name": name}
    response_gender = requests.get(url=URL_GENDER,params=params)
    response_age = requests.get(url=URL_AGE,params=params)
    response_nationality = requests.get(url=URL_NATIONALITY,params=params)
    resp_json_gender = response_gender.json()
    resp_json_age = response_age.json()
    resp_json_nationality = response_nationality.json()

    print(name)
    print(f"{name} is {resp_json_gender['gender']} w prob {resp_json_gender['probability']}")
    print(f" age {resp_json_age['age']}")
    print(f"{name} может быть из \n")
    for i in resp_json_nationality['country']:
        print(f"{i["country_id"]} w prob {i["probability"]}") 

URL_GENDER = "https://api.genderize.io"
URL_AGE = "https://api.agify.io"
URL_NATIONALITY = "https://api.nationalize.io"
get_all_by_name()
# aaaa