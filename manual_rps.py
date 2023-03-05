import random

def get_computer_choice():
    options = ('Rock', 'Paper', 'Scissors')
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice():
    user_choice = input("Please enter 'Rock', 'Paper' or 'Scissors' to play: ")
    return user_choice