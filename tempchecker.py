
def find_highest_temp(cityTemps):
    maxTemp = cityTemps[0][1]
    maxCity = ""
    for location in cityTemps:
        if location[1] >= maxTemp:
            maxTemp = location[1]
            maxCity = location[0]
    #print(f"The hottest city is {maxCity} at {maxTemp} degrees")
    return maxCity, maxTemp


def find_lowest_temp(cityTemps):
    minTemp = cityTemps[0][1]
    minCity = ""
    for location in cityTemps:
        if location[1] <= minTemp:
            minTemp = location[1]
            minCity = location[0]
    #print(f"The hottest city is {maxCity} at {maxTemp} degrees")
    return minCity, minTemp
