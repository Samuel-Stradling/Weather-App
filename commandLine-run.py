from api import maxtemp, mintemp, processTime


print(f"process[{processTime}s]")

maxtempCity = maxtemp[0].replace("+", " ")

print(
    f"\n\nThe hottest place in England currently is {maxtempCity} at {maxtemp[1]} degrees.\n\n\n"
)

mintempCity = mintemp[0].replace("+", " ")
print(
    f"\n\nThe coolest place in England currently is {mintempCity} at {mintemp[1]} degrees.\n\n\n"
)
