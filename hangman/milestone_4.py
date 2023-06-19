import random

word_list = [
    'apple',
    'pear',
    'banana',
    'orange',
    'pineapple'
]

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        word_guessed = []
        for i in range(len(self.word)):
            word_guessed.append('_')
        self.word_guessed = word_guessed
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def ask_for_input(self):
        while True:
            guess = input("Give me a single letter:\n")
            if len(guess) != 1 & guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

    def check_guess(self, guess):
        guess = guess.lower()
        if self.word.find(guess) != -1:
            print(f"Good guess! {guess} is in the word.")
            for j in range(len(self.word)):
                if self.word[j] == guess:
                    self.word_guessed[j] = guess
            print(self.word_guessed)
            self.num_letters = self.num_letters - 1
        else:
            print(f"Sorry, {guess} is not in the word. try again")
            self.num_lives = self.num_lives - 1
            print(f"You have {self.num_lives} lives left.")