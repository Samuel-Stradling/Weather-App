import requests
from cities import cities


with open(r"key.txt", "r") as keyFile:
    api_key = keyFile.readline()

base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_city_temp(city):

    complete_url = base_url + "appid=" + api_key + "&q=" + city

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":
        weather = x["main"]
        current_temp = weather["temp"]
        return round(current_temp - 273.15, 2)
    else:
        print(f"{city} not found")
