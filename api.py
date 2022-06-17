import requests
from cities import cities
from tempchecker import find_highest_temp
import time

tic = time.gmtime()

# api key
with open('key.txt', 'r') as keyFile:
    api_key = keyFile.readline()

base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_temp(city_name):

    # complete url with city name
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    response = requests.get(complete_url)

    # json response object; convert to python format data
    x = response.json()

    # x contains llist of dictionaries
    # if cod = 404, city is not found
    if x["cod"] != "404":

        weather = x["main"]

        current_temperature = weather['temp']
    else:
        print(f"{city_name} not found")
    #print(f"{round((current_temperature - 273.15), 2)}")
    return round((current_temperature - 273.15), 2)


cityTemps = []

for city in cities:
    cityTemps.append([city, get_temp(city)])

maxtemp = find_highest_temp(cityTemps)

toc = time.gmtime()
processTime = abs(tic[5] - toc[5])
