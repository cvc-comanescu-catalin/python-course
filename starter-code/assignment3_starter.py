"""
Assignment 3: Calculator with Functions
=========================================
Build a menu-driven command-line calculator using separate functions.

Topics practiced:
- Defining and calling functions
- Parameters and return values
- while loops with break
- Error handling (division by zero)
- Optional: import math
"""

import math   # Needed for the bonus square_root function


# ─── Arithmetic Functions ─────────────────────────────────────────────────────

def add(a, b):
    """Return the sum of a and b."""
    # TODO: Return a + b
    pass


def subtract(a, b):
    """Return the difference of a and b."""
    # TODO: Return a - b
    pass


def multiply(a, b):
    """Return the product of a and b."""
    # TODO: Return a * b
    pass


def divide(a, b):
    """
    Return the quotient of a divided by b.
    If b is 0, return the string "Error: Cannot divide by zero!"
    """
    # TODO: Check if b is 0; if so, return an error message string
    # Otherwise, return a / b
    pass


# ─── Bonus Functions ──────────────────────────────────────────────────────────

def power(base, exponent):
    """Return base raised to the power of exponent."""
    # TODO: Return base ** exponent
    pass


def square_root(n):
    """
    Return the square root of n.
    If n is negative, return "Error: Cannot take square root of negative number."
    Hint: Use math.sqrt(n)
    """
    # TODO: Check if n is negative; if so, return an error message
    # Otherwise, return math.sqrt(n)
    pass


# ─── UI Functions ─────────────────────────────────────────────────────────────

def display_menu():
    """Print the calculator menu."""
    print("\n" + "=" * 26)
    print("      🧮 Calculator")
    print("=" * 26)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    # TODO (Bonus): Add options 5 and 6 for Power and Square Root
    print("5. Quit")
    print("=" * 26)


def get_two_numbers():
    """
    Ask the user for two numbers.
    Returns a tuple: (num1, num2) as floats.
    """
    # TODO: Ask for the first number and convert to float
    num1 = None  # Replace with: float(input("Enter first number: "))

    # TODO: Ask for the second number and convert to float
    num2 = None  # Replace with: float(input("Enter second number: "))

    return num1, num2


def get_user_choice():
    """
    Ask the user to choose a menu option.
    Returns the choice as a string.
    """
    # TODO: Return the user's menu choice
    # Hint: return input("Choose an option: ").strip()
    pass


# ─── Main Function ────────────────────────────────────────────────────────────

def main():
    """
    Main calculator loop.
    - Display menu
    - Get user's choice
    - Get numbers (if not quitting)
    - Perform the calculation
    - Display the result
    - Loop until quit
    """
    print("Welcome to the Python Calculator! 🧮")

    while True:
        display_menu()
        choice = get_user_choice()

        # TODO: Handle choice "5" (or "6" with bonus) — print goodbye and break

        # TODO: For choices 1-4, call get_two_numbers() then the appropriate function
        # Store the result and print it
        # Example:
        # if choice == "1":
        #     a, b = get_two_numbers()
        #     result = add(a, b)
        #     print(f"Result: {a} + {b} = {result}")
        # elif choice == "2":
        #     ...

        # TODO: Handle invalid menu choice
        # else:
        #     print("Invalid choice. Please enter a number from the menu.")
        pass


if __name__ == "__main__":
    main()
