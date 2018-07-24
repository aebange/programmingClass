import random
import sys
import os
import os.path
import pickle
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 100
SAVEFILEPATH = os.getcwd() + "\\High_Scores.dat"
# Create the random number
randomNumber = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)


# Search dictionary for username defined by user. If already exists, outputs the user's details. Else outputs null
def get_user_details(userName):
    # Open the file using read binary and assign the SAVEFILEPATH to the file_pointer
    if os.stat(SAVEFILEPATH).st_size == 0:
        # File is empty and therefore it is impossible for a user to exist
        return None
    else:
        with open(SAVEFILEPATH, 'rb') as file_pointer:
            # Use pickle.load() to assign the contents of the file designated in file_pointer to user_dict
            user_dict = pickle.load(file_pointer)
            # Check for user's username in pickle file contents
            if userName in user_dict:
                # Username has been found and already exists
                # Assign the user details of username to user_details
                userDetails = user_dict[userName]
                return userDetails
            else:
                # Username has not been found and still needs to be created
                return None


# Takes the new user's desired password and username and installs them into the system. Assigns new default high score
# Case #1:  Adding the first user ever     to a  *empty* file
# Case #2:  Adding 2nd, 3rd, 4th, ... user to an *existing* file
def add_user_details(userID, userPass):
    # Create user details for the new user to be installed into the pickle file
    new_user = {'userid': userID,
                'password': userPass,
                'highscore': 0}
    if os.stat(SAVEFILEPATH).st_size == 0:
        user_dict = {}
        user_dict[userID] = new_user
        with open(SAVEFILEPATH, 'wb') as file_pointer:
            # Use pickle.dump() to write the new contents of user_dict back to the pickle file
            pickle.dump(user_dict, file_pointer)

    else:
        # Open the file using read binary and assign the SAVEFILEPATH to the file_pointer
        with open(SAVEFILEPATH,'rb') as file_pointer:
            # Use pickle.load() to assign the contents of the file designated in file_pointer to user_dict
            user_dict = pickle.load(file_pointer)
            # Adds the new user to the pickle file's contents
        user_dict[userID] = new_user
    # Assigned file pointer to file_pointer using "wb" (write binary)
        with open(SAVEFILEPATH, 'wb') as file_pointer:
            # Use pickle.dump() to write the new contents of user_dict back to the pickle file
            pickle.dump(user_dict, file_pointer)


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
                # Passes the value of localclean_guess to whatever variable the function is assigned to
                return local_clean_guess
        else:
            # User entered a string or something strange - clearing screen
            os.system("cls")
            print("Huh?")


# Retrieve a username from the current user
def prompt_user_for_username():
    print("Please enter your username. If you don't have one, enter whatever user you'd like.")
    user_name = input()
    return user_name


# Initiate the game
def play_the_game(userDetails):
    # Program start
    totalGuessed = 0
    print("Welcome to the guessing game!")
    while True:
        # Passes the parameters for min and max into the function get_clean_number()
        clean_guess = get_clean_number(max=MAXIMUM_NUMBER, min=MINIMUM_NUMBER)
        # Adds to the number of total times the user guessed by 1
        totalGuessed += 1
        os.system("cls")

        # Checks to see if the guess is too low or too high
        if clean_guess > randomNumber:
            print("Your guess of %d was too high, this attempt number %d." % (clean_guess, totalGuessed))
        elif clean_guess < randomNumber:
            print("Your guess of %d was too low, this attempt number %d." % (clean_guess, totalGuessed))
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


# Create a loop to prompt a user for their 4 digit pin. Ensures pin is 4 digits and numeric
def prompt_user_for_password():
    while True:
        os.system('cls')
        print("What is your 4-digit pin?")
        user_password = input()
        if len(user_password) == 4:
            if user_password.isnumeric():
                return user_password
                break
            else:
                print("The 4-digit pin must be composed of numbers 0-9. Please try again.")
        else:
            print("The 4-digit pin must only have 4 charecters.")



# Update the users details in the pickle file
def update_user_to_system(userDetails, UserScore):
    pass


# Program starts here
userName = prompt_user_for_username()
userDetails = get_user_details(userName)


if userDetails == None:
    # user not found im system
    print("You're new to the system, please enter a password")
    userPassword = prompt_user_for_password()
    add_user_details(userName, userPassword)
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
