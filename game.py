# game.py

import random # load the module to avoid `NameError: name 'random' is not defined

print("Rock, Paper, Scissors, Shoot!")

# prompt user for input

user_choice = input("Choose 'rock' or 'paper' or 'scissors'")
print("User chose:")
print(user_choice)

# computer choice at random

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)