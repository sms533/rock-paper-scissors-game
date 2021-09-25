# game.py

import os
from dotenv import load_dotenv
load_dotenv()

import random # load the module to avoid `NameError: name 'random' is not defined

print(os.getenv("PLAYER_NAME"))

print("Welcome Player One to my Rock-Paper-Scissors game...")
print("Rock, Paper, Scissors, Shoot!")

# prompt user for input


user_choice = input("Choose 'rock' or 'paper' or 'scissors'")
if user_choice in ["rock", "paper", "scissors"]:
    print("User chose:")
    print(user_choice)
else:
    print("USER NOT VALID TRY AGAIN")
    exit()

# computer choice at random

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)


if (computer_choice == "rock") and (user_choice == "rock"):
    print("tie")
elif (computer_choice == "paper") and (user_choice == "paper"):
    print("tie")
elif (computer_choice == "scissors") and (user_choice == "scissors"):
    print("tie")
elif (computer_choice == "rock") and (user_choice == "paper"):
    print("you win! :)")
elif (computer_choice == "rock") and (user_choice == "scissors"):
    print("computer wins :(")
elif (computer_choice == "paper") and (user_choice == "rock"):
    print("computer wins :(")
elif (computer_choice == "paper") and (user_choice == "scissors"):
    print("you win! :)")
elif (computer_choice == "scissors") and (user_choice == "rock"):
    print("you win! :)")
elif (computer_choice == "scissors") and (user_choice == "paper"):
    print("computer wins :(")


print("THANKS PLEASE PLAY AGAIN")

