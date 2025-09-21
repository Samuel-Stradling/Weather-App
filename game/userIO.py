import random
from datahandling import get_temperature
from globalcities import cities


def get_user_guess(city):
    """
    Prompts the user to guess the temperature in a specific city until they enter data of correct type.

    Args:
        city (str): The name of the city for which the user is guessing the temperature.

    Returns:
        float: The user's guessed temperature as a floating-point number.
    """
    while True:
        try:
            guessedtemperature = float(
                input(f"Guess the temperatureerature in {city}: ")
            )
            break
        except ValueError:
            print("\nThat was not a valid input. Please try again\n")

    return guessedtemperature


while True:
    # This sets how far a guess needs to be from the real value ± to be correct
    errorInterval = 2

    usrChoice = input("Press q to quit or enter to continue: ")
    if usrChoice.lower() == "q":
        break

    city = random.choice(cities)
    temperature = get_temperature(city)

    if "+" in city:
        city = city.replace("+", " ")

    print(
        f"\n\nYou will have 3 guesses to guess the temperature of the given city within {errorInterval} degrees Celsius."
    )

    guessNumber = 3
    temperatureGuessedCorrectly = False
    while guessNumber > 0:
        print(f"\nYou have {guessNumber} guesses remaining.")

        guessedtemperature = get_user_guess(city)

        if (guessedtemperature >= temperature - errorInterval) and (
            guessedtemperature <= temperature + errorInterval
        ):
            print(
                f"\n\n\nCongratulations! You correctly guessed the temperature in {city} to be close to {temperature} degrees\n\n\n"
            )
            temperatureGuessedCorrectly = True
            guessNumber = 0

        elif guessedtemperature > temperature + errorInterval:
            print()
            print("-" * 20)
            print("it was LOWER")
            print("-" * 20)
            guessNumber -= 1

        elif guessedtemperature < temperature - errorInterval:
            print()
            print("-" * 20)
            print("it was HIGHER")
            print("-" * 20)
            guessNumber -= 1

    if not temperatureGuessedCorrectly:
        print(
            f"Sorry, you didn't get the temperatureerature in {city}, it was actually {temperature} degrees there."
        )
