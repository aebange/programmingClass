import random
import sys
minimumNumber = 1
maximumNumber = 100
totalGuessed = 0

randomNumber = random.randint(minimumNumber,maximumNumber)
print("Welcome to the guessing game")


def get_clean_number(min,max):
    while True:
        print("Enter a number between %d %d" % (min, max))
        rawGuess = input()
        if rawGuess.isnumeric():
            # User entered a numeric value
            localCleanGuess = int(rawGuess)
            if localCleanGuess < min:
                # User entered a number that was outside the range
                print("Your number is too low")
            elif localCleanGuess > max:
                print("Your number is too high")
            else:
                return localCleanGuess
        else:
            # User entered a string or something strange
            print("Huh?")


while True:
    cleanGuess = get_clean_number(minimumNumber,maximumNumber)
    totalGuessed += 1

    if cleanGuess > randomNumber:
        print("You entered a number that was too high")
    elif cleanGuess < randomNumber:
        print("You entered a number that was too low")
    else:
        print("Congratulations, you guessed the number!")
        print("Took you %d guesses.  The random number was %d." % (totalGuessed, randomNumber))
        sys.exit(0)