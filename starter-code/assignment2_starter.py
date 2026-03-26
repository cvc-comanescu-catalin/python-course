"""
Assignment 2: Number Guessing Game
====================================
Build an interactive number guessing game using loops and conditionals.

Topics practiced:
- import random
- while loops
- if/elif/else
- break statement
- Counting attempts
"""

import random


def generate_secret_number(low=1, high=100):
    """
    Generate and return a random integer between low and high (inclusive).

    Parameters:
        low  (int): The lowest possible number (default: 1)
        high (int): The highest possible number (default: 100)

    Returns:
        int: A random integer between low and high
    """
    # TODO: Use random.randint() to generate and return a random number
    # Hint: return random.randint(low, high)
    pass


def get_player_guess():
    """
    Ask the player for a guess and return it as an integer.
    Returns the player's guess as an int.
    """
    # TODO: Ask the player for their guess using input()
    # Convert the input to an integer and return it
    # Hint: return int(input("Your guess: "))
    pass


def check_guess(guess, secret):
    """
    Compare the player's guess to the secret number.
    Print "Too high!", "Too low!", or "Correct!" accordingly.

    Parameters:
        guess  (int): The player's guess
        secret (int): The secret number

    Returns:
        bool: True if the guess is correct, False otherwise
    """
    # TODO: Compare guess to secret
    # If guess == secret: print a success message and return True
    # If guess > secret: print "Too high! Try a lower number." and return False
    # If guess < secret: print "Too low! Try a higher number." and return False
    pass


def play_game():
    """
    Run one complete game session.
    - Generate a secret number
    - Loop: get guess, check guess, count attempts
    - End when correct (or max attempts reached for bonus)
    """
    print("\n🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    # Step 1: Generate the secret number
    # TODO: Call generate_secret_number() and store the result
    secret = None  # Replace with the function call

    # Step 2: Initialize attempts counter
    attempts = 0
    max_attempts = 10   # Used for the bonus

    # Step 3: Game loop
    # TODO: Create a while loop that:
    #   - Increments attempts
    #   - Gets the player's guess
    #   - Calls check_guess()
    #   - Breaks if correct
    #   - (Bonus) Breaks if max_attempts exceeded

    # Example loop structure:
    # while True:
    #     attempts += 1
    #     guess = get_player_guess()
    #     if check_guess(guess, secret):
    #         break
    pass


def main():
    """
    Main function — starts the guessing game.
    For the bonus "play again" feature, wrap play_game() in a loop.
    """
    play_game()

    # BONUS: Ask to play again
    # Uncomment below to add play-again functionality:
    # while True:
    #     play_game()
    #     again = input("\nPlay again? (yes/no): ").strip().lower()
    #     if again != "yes":
    #         print("Thanks for playing! Goodbye!")
    #         break


if __name__ == "__main__":
    main()
