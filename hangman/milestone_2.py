import random

word_list = [
    'apple',
    'pear',
    'banana',
    'orange',
    'pineapple'
]

word = random.choice(word_list)
print(word)

guess = input("Give me a single letter:\n")

if len(guess) == 1:
    print('Good guess!')
else:
    print("Oops! That is not a valid input") 
