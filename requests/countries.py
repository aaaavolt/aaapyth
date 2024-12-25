import requests
import json
import pprint
from prettytable import PrettyTable


def get_country(COUNTRY_NAME):
     URL = f"https://restcountries.com/v3.1/name/{COUNTRY_NAME}"
     try:
        response = requests.get(url=URL)
        response.raise_for_status()
        return response.json()
     except requests.exceptions.RequestException as  e:
        print(f"")
        return None
def extract_user_indo(data):
    user_info = []   
    for user in data:
        name = f"{user['name']['common']}/{user['name']['official']}"
        capital = f"{user['capital']}"
        region = f"{user['region']}|{user['subregion']}"
        population = f"{user['population']}"
        languages = f"{user['languages']}"
        
        user_info.append((name, capital, region, population, languages))
    return user_info  
def get_user_info_table(user_info):
    table = PrettyTable()
    table.field_names = ["имя","столица", "регмон", "популяция", "языки"]
    for info in user_info:
        table.add_row(info)
    return table  
def main():
    COUNTRY_NAME = str(input("!!!"))
    data = get_country(COUNTRY_NAME=COUNTRY_NAME)
    if data:
        print([COUNTRY_NAME])
        user_info  = extract_user_indo(data)
        print(get_user_info_table(user_info=user_info))
    else:
        print()
if __name__ == "__main__":
    main() 
    
    
