import random
import sys
import os
import os.path
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 100
totalGuessed = 0
saveFile = "High_Scores" + '.jpg'
# Create the random number
randomNumber = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)


# Save username to file, assumes file and subdirectory exist
def save_username():
    local_file = open('programFiles:\\%s' % saveFile, 'w')
    local_file.write(userName)
    local_file.close()


# Request user input and ensure that it is both a number within the range and a number that is an integer
def get_clean_number(min, max):
    while True:
        print("Enter a number between %d and %d." % (min, max))
        raw_guess = input()
        if raw_guess.isnumeric():
            # User entered a numeric value
            local_clean_guess = int(raw_guess)
            if local_clean_guess < min:
                # User entered a number that was outside the range
                os.system("cls")
                print("Your number is too low.")
            elif local_clean_guess > max:
                print("Your number is too high.")
            else:
                # Passes the value of localCleanGuess to whatever variable the function is assigned to
                return local_clean_guess
        else:
            # User entered a string or something strange - clearing screen
            os.system("cls")
            print("Huh?")


# Program start
print("Welcome to the guessing game!")
print("What is your username?")
userName = input()
save_username()

while True:
    # Passes the parameters for min and max into the function get_clean_number()
    cleanGuess = get_clean_number(max=MAXIMUM_NUMBER, min=MINIMUM_NUMBER)
    # Adds to the number of total times the user guessed by 1
    totalGuessed += 1

    # Checks to see if the guess is too low or too high
    if cleanGuess > randomNumber:
        os.system('cls')
        print("Your guess of %d was too high, this attempt number %d." % (cleanGuess, totalGuessed))
    elif cleanGuess < randomNumber:
        os.system('cls')
        print("Your guess of %d was too low, this attempt number %d." % (cleanGuess, totalGuessed))
    else:
        os.system('cls')
        print("Congratulations, you successfully guessed the number!")
        print("Took you %d guesses.  The random number was %d." % (totalGuessed, randomNumber))
        print("Press any key to continue...")
        # Use the input as a break point to prevent the program from closing before the user can read the results.
        i = input()
        sys.exit(0)