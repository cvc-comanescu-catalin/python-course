"""
Assignment 1: "About Me" Script
================================
Write a Python script that collects personal information from the user
and displays a nicely formatted summary.

Topics practiced:
- Variables and data types
- User input with input()
- Type conversion (int, float, str)
- String formatting with f-strings
- Basic arithmetic
"""


def get_user_info():
    """
    Ask the user for their name, age, and favorite hobby.
    Returns a tuple: (name, age, hobby)
    """
    # TODO: Ask the user for their name using input()
    name = None  # Replace with: name = input("What is your name? ")

    # TODO: Ask the user for their age and convert it to an integer
    age = None   # Replace with: age = int(input("How old are you? "))

    # TODO: Ask the user for their favorite hobby
    hobby = None  # Replace with: hobby = input("What is your favorite hobby? ")

    return name, age, hobby


def calculate_birth_year(age):
    """
    Calculate the approximate birth year based on the current year and age.
    Returns the birth year as an integer.
    """
    current_year = 2024

    # TODO: Calculate and return the birth year
    # Hint: birth_year = current_year - age
    pass


def display_summary(name, age, birth_year, hobby):
    """
    Display a nicely formatted summary of the user's information.
    """
    # TODO: Print a separator line (e.g., "=" repeated 37 times)
    # Hint: print("=" * 37)

    # TODO: Print a title like "About Me"

    # TODO: Print another separator line

    # TODO: Print the user's name using an f-string
    # Example: f"Hi, I'm {name}!"

    # TODO: Print the user's age and birth year
    # Example: f"I'm {age} years old, born around {birth_year}."

    # TODO: Print the user's hobby
    # Example: f"My favorite hobby is {hobby}."

    # TODO: Print a final separator line
    pass


def bonus_arithmetic():
    """
    BONUS: Ask the user for two numbers and display arithmetic results.
    """
    print("\n--- Bonus: Number Operations ---")

    # TODO: Ask the user for two numbers and convert them to floats
    num1 = None  # Replace with input and float() conversion
    num2 = None  # Replace with input and float() conversion

    # TODO: Print the sum
    # Example: f"{num1} + {num2} = {num1 + num2}"

    # TODO: Print the difference

    # TODO: Print the product

    # TODO: Print the quotient — handle division by zero!
    # Hint: if num2 != 0: ... else: print("Cannot divide by zero!")
    pass


def main():
    """
    Main function — runs the About Me program.
    """
    # Step 1: Get user information
    name, age, hobby = get_user_info()

    # Step 2: Calculate birth year
    birth_year = calculate_birth_year(age)

    # Step 3: Display the summary
    display_summary(name, age, birth_year, hobby)

    # Step 4 (Bonus): Do arithmetic with two numbers
    # Uncomment the line below to include the bonus section:
    # bonus_arithmetic()


# This block runs when you execute this file directly
if __name__ == "__main__":
    main()
