def get_temperature(city_name):
    """
    Retrieves the current temperature for a given city using the OpenWeatherMap API.

    Args:
        city_name (str): The name of the city for which the temperature is requested.

    Returns:
        float: The current temperature in Celsius for the specified city.

    Raises:
        ValueError: If the API response indicates that the city was not found.

    This function uses the OpenWeatherMap API to fetch the current temperature for a
    specified city. It requires a valid API key, which is stored in a 'key.txt' file
    located in the main project folder. The function reads the API key from the file
    and constructs the API request URL with the city name and the API key.

    Note: The 'key.txt' file should contain only the API key as the first line, and no
    other content.
    """
    import requests
    import os

    # Get the current directory of the script
    workingDir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the key txt file in the main project folder
    keyTxtPath = os.path.join(workingDir, "..", "key.txt")

    # API KEY DIRECTORY, MAY NEED TO CHANGE DEPENDING ON WHERE IT IS STORED
    APIKeyDirectory = keyTxtPath

    with open(APIKeyDirectory, "r") as keyFile:
        api_key = keyFile.readline()

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # complete url with city name
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    responseJson = response.json()

    # x contains list of dictionaries
    # if cod = 404, city is not found
    if responseJson["cod"] != "404":
        weatherData = responseJson["main"]
        # main contains another dictionary witht he main temperature for that city

        current_temperature = weatherData["temp"]
    else:
        raise ValueError()
    return round((current_temperature - 273.15), 2)
