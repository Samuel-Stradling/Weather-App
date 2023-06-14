import random
from datahandling import get_temp
from globalcities import cities

running = True
#is this really true
while running:
    errorInterval = 2
    randomIndex = random.randint(0, len(cities) - 1)
    usrChoice = input("Press q to quit or enter to continue: ")
    if usrChoice.lower() == "q":
        running = False
        break

    print(
        f"\n\nYou will have 3 guesses to guess the temperature of the given city within {errorInterval} degrees Celsius."
    )

    city = cities[randomIndex]
    if "+" in city:
        city = city.replace("+", " ")

    temp = get_temp(cities[randomIndex])

    guessNo = 3
    while guessNo > 0:
        print(f"\nYou have {guessNo} guesses remaining.")
        guessTemp = float(input(f"Guess the temperature in {city}: "))
        print("\n")
        if (guessTemp > temp - errorInterval) and (guessTemp < temp + errorInterval):
            print(
                f"Congratulations! You correctly guessed the temperature in {city} to be close to {temp} degrees"
            )
            break
        guessNo -= 1
        if guessTemp > temp + errorInterval and guessNo != 1:
            print("Lower")
        elif guessTemp < temp - errorInterval and guessNo != 1:
            print("Higher")

        if guessNo == 0:
            print(
                f"Sorry, you didn't get the temperature in {city}, it was actually {temp} degrees there."
            )
