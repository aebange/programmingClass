import random
import sys
import os
import os.path
import pickle
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 100
totalGuessed = 0
SAVEFILEPATH = os.getcwd() + "/High_Scores"
# Create the random number
randomNumber = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)


# 1. Open pickle file
# 2. Convert the file into a dictionary
# 3. Search dictionary for username defined by user and return null if nothing found or userID if it is found\
def get_user_details(userID):


def add user_details(userID, userPass)


# Save username to file, assumes file and subdirectory exist
def save_data():
    file_pointer = open(SAVEFILEPATH % saveFile, 'w')


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
userName = prompt_user_for_username()

userDetails = get_user_details()

if userDetails == None:
    # user not found im system
else

    while True:
        userPassword = prompt_user_for_Password()
        if userPassword != userDetails:
            print("Wrong password, try again")

    runProgram()

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