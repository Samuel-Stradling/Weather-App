
def find_highest_temp(cityTemps):
    maxTemp = 0
    maxCity = ""
    for location in cityTemps:
        if location[1] > maxTemp:
            maxTemp = location[1]
            maxCity = location[0]
    print(f"The hottest city is {maxCity} at {maxTemp} degrees")
