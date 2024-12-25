import requests

import pprint
import json
from prettytable import PrettyTable
def get_random_users_data(NUM_RESULT=5, QUERY = "гарри"):


    url = f"https://www.googleapis.com/books/v1/volumes?q={QUERY}&maxResults={NUM_RESULT}&langRestrict=ru"
    try:
        response = requests.get(url=url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as  e:
        print(f"")
        return None

def extract_user_indo(data):
    user_info = [
    ]   
    for user in data['results']:
        name = f"{user['name']['first']}{user['name']['last']}"
        gender = f"{user['gender']}"
        email = f"{user['email']}"
        country = f"{user['location']['country']}"
        age = f"{user['dob']['age']}"
        user_info.append((name, gender, age, email, country))
    return user_info
def get_user_info_table(user_info):
    table = PrettyTable()
    table.field_names = ["имя","пол", "возраст", "эмаил", "страна"]
    for info in user_info:
        table.add_row(info)
    return table
def main():
    NUM_RESULT = int(input("!!!"))
    data = get_random_users_data(NUM_RESULT=NUM_RESULT)
    if data:
        print([NUM_RESULT])
        user_info  = extract_user_indo(data)
        print(get_user_info_table(user_info=user_info))
    else:
        print()
if __name__ == "__main__":
    main()