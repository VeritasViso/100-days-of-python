## Made by @VeritasViso on 21/04/2026 at 14:56pm.

# Rock, Paper, Scissors project (Day 4 of 100)

import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

computer_choice = random.randint(0, 2)

try:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    print(f"You chose: {options[user_choice]}")
    print(f"Computer chose: {options[computer_choice]}")
    ## user LOSING
    if user_choice == 0 and computer_choice == 1 or user_choice == 1 and computer_choice == 2 or user_choice == 2 and computer_choice == 0:
        print("You lose")
    ## user DRAWING
    elif user_choice == 0 and computer_choice == 0 or user_choice == 1 and computer_choice == 1 or user_choice == 2 and computer_choice == 2:
        print("It's a draw.")
    ## user WINNING
    elif user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
        print("You win!")
except:
    print("You didn't type 0, 1 or 2.")
