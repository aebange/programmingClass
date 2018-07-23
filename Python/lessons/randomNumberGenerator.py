import random
import sys
import os
import os.path
import pickle
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 100
SAVEFILEPATH = os.getcwd() + "/High_Scores"
# Create the random number
randomNumber = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)


# 1. Open pickle file
# 2. Convert the file into a dictionary
# 3. Search dictionary for username defined by user and return null if nothing found or userID if it is found\
def get_user_details(userID):
    pass


def add_user_details(userID, userPass):
    pass


#
# # Save username to file, assumes file and subdirectory exist
# def save_data():
#     file_pointer = open(SAVEFILEPATH % saveFile, 'w')
#

# Request user input and ensure that it is both a number within the range and a number that is an integer
# Convert the user's inputted guess to a clean number


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


# Retrieve a username from the current user
def prompt_user_for_username():
    pass


# Initiate the game
def play_the_game(userDetails):
    # Program start
    totalGuessed = 0
    print("Welcome to the guessing game!")
    while True:
        # Passes the parameters for min and max into the function get_clean_number()
        cleanGuess = get_clean_number(max=MAXIMUM_NUMBER, min=MINIMUM_NUMBER)
        # Adds to the number of total times the user guessed by 1
        totalGuessed += 1
        os.system('cls')

        # Checks to see if the guess is too low or too high
        if cleanGuess > randomNumber:
            print("Your guess of %d was too high, this attempt number %d." % (cleanGuess, totalGuessed))
        elif cleanGuess < randomNumber:
            print("Your guess of %d was too low, this attempt number %d." % (cleanGuess, totalGuessed))
        else:
            print("Congratulations, you successfully guessed the number!")
            print("Took you %d guesses.  The random number was %d." % (totalGuessed, randomNumber))
            break

    return totalGuessed


# Create a break in operations to provide the user an opportunity to read the screen output
def press_any_key():
    print("Press any key to continue...")
    # Use the input as a break point to prevent the program from closing before the user can read the results.
    i = input()


# Create a loop to prompt a user for their 4 digit pin
def prompt_user_for_password():
    print("What is your 4-digit pin?")
    user_Password =  input()


# Update the users details in the pickle file
def update_user_to_system(userDetails):
    pass


# Save the users details to the pickle file
def add_user_to_system(userName, userPassword):
    pass


# Program starts here
userName = prompt_user_for_username()
userDetails = get_user_details()


if userDetails == None:
    # user not found im system
    print("You're new to the system, please enter a password")
    userPassword = prompt_user_for_password()
    add_user_to_system(userName, userPassword)
else:
    print("User found, please enter your password")
    while True:
        userPassword = prompt_user_for_password()
        actualPasswordFromFile = userDetails.get("password")
        if userPassword != actualPasswordFromFile:
            print("Wrong password, try again")
        else:
            # User entered correct password, break out of the loop
            break

    userScore = play_the_game(userDetails)

    update_user_to_system(userDetails, userScore)

    press_any_key()
