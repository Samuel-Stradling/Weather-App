import requests
import os
from globalcities import cities as citiesTuple  # tuple containing england cities

# Get the current directory of the script
workingDir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the key txt file in the main project folder
keyTxtPath = os.path.join(workingDir, '..', 'key.txt')

# API KEY DIRECTORY, MAY NEED TO CHANGE DEPENDING ON WHERE IT IS STORED
APIKeyDirectory = keyTxtPath


with open(APIKeyDirectory, "r") as keyFile:
    api_key = keyFile.readline()


base_url = "http://api.openweathermap.org/data/2.5/weather?"


def get_temperature(city_name):
    """Returns the temperature of a given city.

    If the argument 'city_name' is not found in the API repsonse, raises ValueError

    Parameters
    -------------
    city_name : str
        The name of the city in England to get the temperature of

    Raises
    -------------
    ValueError
        If the city_name is not found in the

    """

    # complete url with city name
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    response = requests.get(complete_url)

    # json response object; convert to python format data
    responseJson = response.json()

    # x contains llist of dictionaries
    # if cod = 404, city is not found
    if responseJson["cod"] != "404":
        weatherData = responseJson["main"]
        # main contains another dictionary witht he main temperature for that city

        current_temperature = weatherData["temp"]
    else:
        raise ValueError()
    return round((current_temperature - 273.15), 2)


cityTemps = {}
for city in citiesTuple:
    try:
        cityTemps[city] = get_temp(city)
    except ValueError:
        print(f"No data found for {city}")
        continue


hottestCity = max(cityTemps, key=cityTemps.get)
hottestTemp = cityTemps[hottestCity]

coolestCity = min(cityTemps, key=cityTemps.get)
coolestTemp = cityTemps[coolestCity]


