import random
import sys
import os
import os.path
import pickle

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 500
SAVEFILEPATH = os.getcwd() + "\\High_Scores.dat"
# Create the random number
randomNumber = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)


# Search dictionary for username defined by user. If already exists, outputs the user's details. Else outputs null
def get_user_details(user_name):
    # Open the file using read binary and assign the SAVEFILEPATH to the file_pointer
    if not os.path.isfile(SAVEFILEPATH):
        # File does not existr. So, return none as the user does not exist in the system
        return None
    elif os.stat(SAVEFILEPATH).st_size == 0:
        # Data file exists but it's an empty file: therefore it is impossible for a user to exist
        return None
    else:
        # Data file exists and is not empty
        with open(SAVEFILEPATH, 'rb') as file_pointer:
            # Use pickle.load() to assign the contents of the file designated in file_pointer to user_dict
            user_dict = pickle.load(file_pointer)
            # Check for user's username in pickle file contents
            if user_name in user_dict:
                # Username has been found and already exists
                # Assign the user details of username to user_details
                userDetails = user_dict[user_name]
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
    if (os.path.isfile(SAVEFILEPATH) == False) or (os.stat(SAVEFILEPATH).st_size == 0):
        # Case #1:  The data file is empty or data file does not exist
        user_dict = {}
        user_dict[userID] = new_user

        # Create a new file or append to write to the empty file
        with open(SAVEFILEPATH, 'wb') as file_pointer:
            # Use pickle.dump() to write the new contents of user_dict back to the pickle file
            pickle.dump(user_dict, file_pointer)
    else:
        # Case #2:  The data file is not empty
        # -- Open the file using read binary and assign the SAVEFILEPATH to the file_pointer
        with open(SAVEFILEPATH, 'rb') as file_pointer:
            # Use pickle.load() to assign the contents of the file designated in file_pointer to user_dict
            user_dict = pickle.load(file_pointer)
            # Adds the new user to the pickle file's contents
        user_dict[userID] = new_user
        # Assigned file pointer to file_pointer using "wb" (write binary)
        with open(SAVEFILEPATH, 'wb') as file_pointer:
            # Use pickle.dump() to write the new contents of user_dict back to the pickle file
            pickle.dump(user_dict, file_pointer)

    # Always return the user details of the new user
    return new_user


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
        elif raw_guess == 'AC':
            print("Invoked autocomplete")
            raw_guess = randomNumber
            local_clean_guess = int(raw_guess)
            return local_clean_guess
        else:
            # User entered a string or something strange - clearing screen
            os.system("cls")
            print("Huh?")


# Retrieve a username from the current user
def prompt_user_for_username():
    while True:
        os.system("cls")
        print("Please enter your username. If you don't have one, enter whatever user you'd like.")
        user_name = input()
        if user_name == "list_users":
            with open(SAVEFILEPATH, 'rb') as file_pointer:
                # Use pickle.load() to assign the contents of the file designated in file_pointer to user_dict
                complete_dict = pickle.load(file_pointer)
                complete_dict_list = list(complete_dict)
                # while True:
                # item_number = 0
                print(complete_dict_list)
                print("Press enter to continue...")
                input()
        elif user_name == "delete_users":
            while True:
                print('Who would you like to remove? Type "exit" to exit.')
                user_target = input()
                if user_target == "exit":
                    break
                else:
                    with open(SAVEFILEPATH, 'rb') as file_pointer:
                        # Use pickle.load() to assign the contents of the file designated in file_pointer to user_dict
                        complete_dict = pickle.load(file_pointer)
                        if user_target in complete_dict:
                            del complete_dict[user_target]
                            with open(SAVEFILEPATH, 'wb') as file_pointer:
                                # Use pickle.dump() to write the new contents of user_dict back to the pickle file
                                pickle.dump(complete_dict, file_pointer)
                            print("User %s has been brutally murdered." % user_target)
                        else:
                            print("Could not identify user %s..." % user_target)
        else:
            return user_name


# Initiate the game
def play_the_game():
    # Program start
    totalGuessed = 0
    print("Welcome back to the guessing game %s!" % userName)
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
    print('Press enter to play again. If you would like to stop, type "exit"')
    user_choice = input()
    if user_choice == 'exit':
        sys.exit()
    elif user_choice == 'Exit':
        sys.exit()
    else:
        print("Restarting game!")


# Create a loop to prompt a user for their 4 digit pin. Ensures pin is 4 digits and numeric
def prompt_user_for_password():
    while True:
        print("What is your 4-digit pin?")
        user_password = input()
        if len(user_password) == 4:
            if user_password.isnumeric():
                return user_password
            else:
                os.system('cls')
                print("The 4-digit pin must be composed of numbers 0-9. Please try again.")
        else:
            os.system('cls')
            print("The 4-digit pin must only have 4 charecters.")


# Update the users details in the pickle file
def update_user_to_system(userName, userDetails):
    # Open the file using read binary and assign the SAVEFILEPATH to the file_pointer
    if os.stat(SAVEFILEPATH).st_size == 0:
        # File is empty and therefore it is impossible for a user to exist
        print("User save file has been corrupted and score cannot be saved to it.")
        return None
    else:
        with open(SAVEFILEPATH, 'rb') as file_pointer:
            # Use pickle.load() to assign the contents of the file designated in file_pointer to user_dict
            updated_user_dict = pickle.load(file_pointer)
            # Check for user's username in pickle file contents
            if userName in updated_user_dict:
                # Username has been found and already exists
                # Assign the pregenerated userDetails of username to updated_user_details
                updated_user_dict[userName] = userDetails
                with open(SAVEFILEPATH, 'wb') as file_pointer:
                    # Use pickle.dump() to update the new contents of updated_user_dict back to the pickle file
                    pickle.dump(updated_user_dict, file_pointer)
            else:
                # Username has not been found and still needs to be created
                return None


# Compares the user's new score with their old best scores to see if the score should be updated
def update_user_score(userDetails, userScore):
    if userDetails['highscore'] == 0:
        # User score has never been recorded before, setting first score as new highscore
        print("This was your first time playing, so your new highscore is %d." % userScore)
        userDetails['highscore'] = userScore
        return userDetails
    elif userDetails['highscore'] > userScore:
        # User score has been improved (less is better) and will be updated
        print("You beat your previous high score of %d." % userDetails['highscore'])
        userDetails['highscore'] = userScore
        return userDetails
    else:
        # User score is worse than it previously was and will be discarded
        print("You did not beat your high score of %d." % userDetails['highscore'])
        return userDetails


# Program starts here
while True:
    os.system('cls')
    # Prompt the user for their username
    userName = prompt_user_for_username()
    # Retrieve the userdetails for that username from the file
    userDetails = get_user_details(userName)
    # Check to see if the user exists, if not prompt them to enter a new password
    # If the user exists, ask them for their password until they get it correct
    if userDetails == None:
        # user not found im system
        print("You're new to the system, please enter a password")
        userPassword = prompt_user_for_password()
        userDetails = add_user_details(userName, userPassword)
    else:
        while True:
            userPassword = prompt_user_for_password()
            actualPasswordFromFile = userDetails.get("password")
            if userPassword != actualPasswordFromFile:
                print("Wrong password, try again")
            else:
                # User entered correct password, break out of the loop
                os.system('cls')
                break
    # Begin the game, record the user's score to userScore
    userScore = play_the_game()
    # Check the user's score to see if it has improved. If it has, send the new value to our local copy of the pickle dict
    update_user_score(userDetails, userScore)
    # Overwrite the pickle file's version of the current users data with the new local version
    update_user_to_system(userName, userDetails)
    # Prompt the user to make sure that they get a chance to read what is on the screen
    press_any_key()
