import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letter in secret_word:
        if(letter == letters_guessed):
            return True
        else:
            return False
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    correct_words = ""

    for i in range(0, len(secret_word)):
        match = False
        for j in range(0, len(letters_guessed)):
            if(secret_word[i] == letters_guessed[j]):
                match = True

        if match == True:
            correct_words += secret_word[i]
        else:
            correct_words += "-"

    return correct_words



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False


# user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# checks if user entered one letter
def check_letters(letter):
    check = False

    while (check == False):
        if(len(letter) > 1):
            print("That's more than one letter, please enter one letter only")
            letter = user_input("Enter a letter: ")

        elif (letter.isspace() == True):
            print("That's a white space, please enter a letter only")
            letter = user_input("Enter a letter: ")

        else:
            check = True

    return letter

def draw_spaceman():
    spaceman = """                      <>\n"""
    spaceman += """        .-'""-.       ||::::::==========\n"""
    spaceman += """       /= ___  \\      ||::::::==========\n"""
    spaceman += """      |- /~~~\\  |     ||::::::==========\n"""
    spaceman += """      |=( '.' ) |     ||================\n"""
    spaceman += """      \\__\\_=_/__/     ||================\n"""
    spaceman += """       {_______}      ||================\n"""
    spaceman += """     /` *       `'--._||\n"""
    spaceman += """    /= .     [] .     { >\n"""
    spaceman += """   /  /|ooo     |`'--'||\n"""
    spaceman += """  (   )\\_______/      ||\n"""
    spaceman += """   \\``\\/       \\      ||\n"""
    spaceman += """`    -| ==    \\_|     ||\n"""
    spaceman += """      /         |     ||\n"""
    spaceman += """     |=   >\\  __/     ||\n"""
    spaceman += """     \\   \\ |- --|     ||\n"""
    spaceman += """      \\ __| \\___/     ||\n"""
    spaceman += """      _{__} _{__}     ||\n"""
    spaceman += """     (    )(    )     ||\n"""
    spaceman += """^^~  `"''''  `''''  ~^^^~^^~~~^^^~^^^~^^^~^^~^\n"""


    print(spaceman)

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    word = ""
    letters = ""
    end_game = False
    round = 7

    print(secret_word)

    #TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman!")
    print("The secret word contains: "+str(len(secret_word))+" letters")
    print("You have 7 incorrect guesses, please enter one letter per round")
    print("-------------------------------------")


    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    while(end_game == False):
        letter = check_letters(user_input("Enter a letter: "))

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if(is_guess_in_word(letter, secret_word)):
            print("Your guess appears in the word!")
            letters += letter
        else:
            print("Sorry your guess was not in the word, try again")
            draw_spaceman()
            round -= 1


    #TODO: show the guessed word so far
        word = get_guessed_word(secret_word, letters)
        print("Your guess so far: "+word)

    #TODO: check if the game has been won or lost
        if(word == secret_word):
            print("Game ended! You've Won")
            end_game = True

        elif(round < 1):
            end_game = True


#These function calls that will start the game
secret_word = load_word()
spaceman(load_word())
