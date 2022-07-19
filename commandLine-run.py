from api import maxtemp, mintemp, processTime


print(f"process[{processTime}s]")

maxtempCity = maxtemp[0].replace("+", " ")
if "," in maxtemp[0]:
    commaIndex = maxtemp[0].index(",")
    betterCityName = maxtemp[0][0:commaIndex]
    maxtempCity =  betterCityName

print(
    f"\n\nThe hottest place in England currently is {maxtempCity} at {maxtemp[1]} degrees.\n\n\n"
)

mintempCity = mintemp[0].replace("+", " ")
if "," in mintemp[0]:
    commaIndex = mintemp[0].index(",")
    betterCityName = mintemp[0][0:commaIndex]
    mintempCity = betterCityName
print(
    f"\n\nThe coolest place in England currently is {mintempCity} at {mintemp[1]} degrees.\n\n\n"
)
