import re
from datahandling import processTime, hottestCity, hottestTemp, coolestCity, coolestTemp


def format_city_name(city_name):
    if "+" in city_name:
        city_name = city_name.replace("+", " ")

    match = re.search(r"(.+)(?=, GB)", city_name)
    if match:
        city_name = match.group(1)
    return city_name


print(f"process[{processTime}s]")

print(f"The hottest city was {format_city_name(hottestCity)} at {hottestTemp}°C")
print()
print(f"The coolest city was {format_city_name(coolestCity)} at {coolestTemp}°C")
