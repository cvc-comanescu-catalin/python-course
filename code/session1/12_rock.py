"""
Rock, Paper, Scissors is a simple game where two players simultaneously choose one of three options: rock, paper, or scissors. The rules are as follows:
- Rock beats scissors (rock crushes scissors)
- Scissors beats paper (scissors cut paper)
- Paper beats rock (paper covers rock)
The game can be played in a single round or in multiple rounds, and the player with the most wins at the end is declared the overall winner.
In this code snippet, we will implement a simple version of the Rock, Paper, Scissors game in Python, allowing a user to play against the computer.
"""

import random
# use random integer to select a random option for the computer to play against the user
computer_choice = random.randint(0, 2)  # Random integer between 0 and 2 (inclusive)
# assume 0 = rock, 1 = paper, 2 = scissors

if computer_choice == 0:
    computer_choice = "rock"
elif computer_choice == 1:
    computer_choice = "paper"
else:
    computer_choice = "scissors"

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

if user_choice == computer_choice:
    print(f"Both chose {user_choice}. It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
     print(f"You win! {user_choice} beats {computer_choice}.")
elif user_choice == "paper" and computer_choice == "rock":
    print(f"You win! {user_choice} beats {computer_choice}.")
elif user_choice == "scissors" and computer_choice == "paper":
    print(f"You win! {user_choice} beats {computer_choice}.")
else:
    print(f"You lose! {computer_choice} beats {user_choice}.")