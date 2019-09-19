from spaceman import is_guess_in_word, get_guessed_word, check_letters
import pytest

# This function checks if the first argument is contained
# within the second agrument and returns a boolean
def test_is_guess_in_word():
    assert is_guess_in_word("ta", "task")
    assert is_guess_in_word("1", "ice") == False, "Invalid user input, number letter"
    assert is_guess_in_word(" ", "car") == False, "Invalid user input, white space"
    assert is_guess_in_word("ascasdc", "house") == False, "Invalid user input, incorrect guess"

# This function takes in a secrect word as first agument and guessed
# letters in the second argument to return a string with the correct
# letters at corresponding indexes or -
def test_get_guessed_word():
    assert get_guessed_word("car", "car") == "car", "guessed word is not correct"
    assert get_guessed_word("car", "rac") == "car", "guessed word is not correct"
    # assert get_guessed_word("car", "dog") == "car", "Invalid user input, incorrect guess"
    # assert get_guessed_word("car", "1 2") == "car", "Invalid user input, incorrect guess"

# This function checks if the user input is one letter only and not a white space
# otherwise, it will ask the user again to enter an input.
def test_check_letters():
    assert check_letters("a")
    assert check_letters("b")
    assert check_letters("1")

# start
if __name__ == '__main__':
    test_is_guess_in_word()
    test_get_guessed_word()
    test_check_letters()
