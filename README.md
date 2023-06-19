# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Milestone 2

Added a file 'milestone_2.py' which does the following:
    -- Creates a list of words based on fruit
    -- Chooses one at random using the random package
    -- asks the user for a single letter input
    -- verifies the users input is just one letter

# Milestone 3

Added the file 'milestone_3.py' which does the following:
    -- Generates a random word for the user to guess
    -- includes an 'ask_for_input' function which prompts the user to guess a letter
    -- includes a 'check_guess' function which is called to make sure the guess is a valid single character.

# Milestone 4

Added the file 'milestone_4.py' which does the following:
    -- Creates an instance of the 'Hangman' class which includes methods allowing you to play the classes hangman game.
    -- You must provide the Hangman class with a word list to use, optionally you can also pass it the number of lives, e.g. Hangman(word_list, 4)
    -- It has an 'ask_for_input' method to start the game, it will ask the user for a single letter.
    -- After each guess the 'check_guess' method is called to make sure it is a valid guess, and record what has been guessed and how many lives are left.

# Milestone 5

Added the file milestone_5.py which allows you to play the Hangman game. This is done by a new function called 'play_game'.
    -- The play_game function takes in a word_list and sets a number of lives in the num_lives variable.
    -- It then initiates the Hangman class to set the game parameters
    -- The function then loops through the ask_for_input() method.
The game is lost when you run out of lives. If you do manage to guess all the letters, you win the game.