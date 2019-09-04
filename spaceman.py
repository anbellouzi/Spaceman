import random

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if(letter == letters_guessed):
            return True
        else:
            return False


def get_guessed_word(secret_word, letters_guessed):
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

#These function calls that will start the game
def start_game():
    secret_word = load_word()
    spaceman(load_word())

def spaceman(secret_word):
    word = ""
    letters = ""
    end_game = False
    round = len(secret_word)
    all_letters = ""

    #TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman!")
    print("The secret word contains: "+str(len(secret_word))+" letters")
    print("You have "+str(round)+" incorrect guesses, please enter one letter per round")
    print("-------------------------------------")

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    while(end_game == False):
        letter = check_letters(user_input("Enter a letter: "))

        if(is_guess_in_word(letter, word)):
            print("You've already guessed that letter")

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if(is_guess_in_word(letter, secret_word)):
            print("Your guess appears in the word!")
            letters += letter
            all_letters += letter

        elif(letter in all_letters):
            print("You've already guess that letter: "+letter)

        else:
            round -= 1
            print("Sorry your guess was not in the word, try again")
            draw_spaceman()
            print("You have "+str(round)+" guesses left!")
            all_letters += letter

    #TODO: show the guessed word so far
        word = get_guessed_word(secret_word, letters)
        print("Your guess so far: "+word)

    #TODO: check if the game has been won or lost
        if(word == secret_word):
            print("Game ended! You've Won")
            end_game = True

        elif(round < 1):
            print("Sorry you lost! The secret word is: "+secret_word)
            end_game = True

    play_again = check_letters(user_input("Do you want to play the game again?: y/n "))
    if(play_again == "y"):
        print("Great! game is starting...\n")
        start_game()

    elif(play_again == "n"):
        print("Goodbye!")
        draw_spaceman()

start_game()
