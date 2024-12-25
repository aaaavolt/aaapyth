import requests
import configparser

import pprint
import json
from prettytable import PrettyTable
def get_apikey(filename="requests/config.ini"):
    conf = configparser.ConfigParser()
    conf.read(filename)
    my_api_key = conf.get('api','api_key')
    print(f"key is - {my_api_key}")
    return my_api_key
def get_random_users_data(city="moscow", api_key = ""):
    if (api_key == ""):
        api_key = get_apikey()


    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    try:
        response = requests.get(url=url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as  e:
        print(f"{e}")
        return None

def extract_user_indo(data):
    print(data)
    if data:
        city_name = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']

        print((city_name, temperature,humidity,weather_description,wind_speed))
        return (city_name, temperature,humidity,weather_description,wind_speed)
    return None
def get_user_info_table(user_info):
    table = PrettyTable()
    table.field_names = ["город","темп", "влажность", "описание","прешур"]

    table.add_row(user_info)
    return table
def main():
    city = input("!!!")
    
    data = get_random_users_data(city)
    if data:
        
        user_info  = extract_user_indo(data)
        print(user_info)
        print(get_user_info_table(user_info=user_info))
    else:
        print()
if __name__ == "__main__":
    main()