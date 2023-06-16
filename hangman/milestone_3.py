import random

word_list = [
    'apple',
    'pear',
    'banana',
    'orange',
    'pineapple'
]

word = random.choice(word_list)

def ask_for_input():
    while True:
        guess = input("Give me a single letter:\n")
        if len(guess) == 1 & guess.isalpha():
            check_guess(guess)
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def check_guess(guess):
    guess = guess.lower()
    if word.find(guess) != -1:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. try again")

ask_for_input()