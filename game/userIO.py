import random
from api import get_city_temp
from cities import cities

running = True
while running:
    errorInterval = 3
    randomIndex = random.randint(0, len(cities) - 1)
    usrChoice = input("Press q to quit or enter to continue: ")
    if usrChoice.lower() == "q":
        running = False
        break

    print(f"\n\nYou will have 3 guesses to guess the temperature of the given city within {errorInterval} degrees Celsius.")

    city = cities[randomIndex]
    if "+" in city:
        city = city.replace("+", " ")

    temp = get_city_temp(cities[randomIndex])

    guessNo = 3
    while guessNo > 0:
        print(f"\nYou have {guessNo} guesses remaining.")
        guessTemp = int(input(f"Guess the temperature in {city}: "))
        print("\n")
        if (guessTemp > temp - errorInterval) and (guessTemp < temp + errorInterval):
            print(
                f"Congratulations! You correctly guessed the temperature in {city} to be close to {temp} degrees")
            break
        guessNo -= 1
        if guessNo == 0:
            print(
                f"Sorry, you didn't get the temperature in {city}, it was actually {temp} degrees there.")
