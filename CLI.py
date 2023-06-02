import re, time


def format_city_name(city_name):
    if "+" in city_name:
        city_name = city_name.replace("+", " ")

    match = re.search(r"(.+)(?=, GB)", city_name)
    if match:
        city_name = match.group(1)
    return city_name


def main():
    tic = time.gmtime()  # starts the timer for the process
    from datahandling import hottestCity, hottestTemp, coolestCity, coolestTemp
    toc = time.gmtime()  # ends the timer for the process

    processTime = abs(tic[5] - toc[5])
    print(f"process[{processTime}s]")

    
    
    
    print(f"The hottest city was {format_city_name(hottestCity)} at {hottestTemp}°C")
    print()
    print(f"The coolest city was {format_city_name(coolestCity)} at {coolestTemp}°C")

if __name__ == "__main__":
    main()
