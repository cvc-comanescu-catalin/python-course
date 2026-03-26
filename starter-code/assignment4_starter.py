"""
Assignment 4: Student Gradebook
=================================
Build a menu-driven gradebook application using dictionaries.

Topics practiced:
- Dictionaries (create, read, update, delete)
- Looping over dictionaries
- Functions with parameters
- Input validation
- f-string formatting
"""


# ─── Gradebook Operations ─────────────────────────────────────────────────────

def add_student(gradebook):
    """
    Ask the user for a student name and grade, then add them to the gradebook.

    Parameters:
        gradebook (dict): The dictionary to add the student to
                          key = student name (str), value = grade (float)
    """
    # TODO: Ask for the student's name
    name = None  # Replace with: input("Enter student name: ").strip()

    # TODO: Ask for the grade and validate it (must be 0-100)
    # Hint: Use try/except for ValueError, and check 0 <= grade <= 100
    # If valid, add to gradebook: gradebook[name] = grade
    # If invalid, print an error message

    # Example structure:
    # try:
    #     grade = float(input("Enter grade (0-100): "))
    #     if 0 <= grade <= 100:
    #         gradebook[name] = grade
    #         print(f"✓ Added {name} with grade {grade}.")
    #     else:
    #         print("Grade must be between 0 and 100!")
    # except ValueError:
    #     print("Please enter a valid number for the grade.")
    pass


def view_all_students(gradebook):
    """
    Display all students and their grades.
    If the gradebook is empty, print "No students yet."

    Parameters:
        gradebook (dict): key = student name, value = grade
    """
    # TODO: Check if gradebook is empty
    # Hint: if not gradebook:

    # TODO: Print a formatted header

    # TODO: Loop through gradebook.items() and print each student's name and grade
    # Hint: for name, grade in gradebook.items():
    #     print(f"{name:<15} → {grade:>5.1f}")
    pass


def search_student(gradebook):
    """
    Ask for a student name and display their grade if found.

    Parameters:
        gradebook (dict): key = student name, value = grade
    """
    # TODO: Ask for the student's name to search for
    name = None  # Replace with: input("Enter student name to search: ").strip()

    # TODO: Check if the name is in the gradebook and print the result
    # Hint: if name in gradebook:
    #     print(f"{name}'s grade: {gradebook[name]}")
    # else:
    #     print(f"Student '{name}' not found.")
    pass


def calculate_average(gradebook):
    """
    Calculate and print the class average grade.
    If the gradebook is empty, print "No students to average."

    Parameters:
        gradebook (dict): key = student name, value = grade
    """
    # TODO: Handle empty gradebook case

    # TODO: Calculate the average
    # Hint: avg = sum(gradebook.values()) / len(gradebook)

    # TODO: Print the average formatted to 2 decimal places
    # Hint: print(f"Class average: {avg:.2f}")
    pass


def display_menu():
    """Print the gradebook menu options."""
    print("\n" + "=" * 34)
    print("       📚 Student Gradebook")
    print("=" * 34)
    print("1. Add student")
    print("2. View all students")
    print("3. Search for a student")
    print("4. Calculate class average")
    # TODO (Bonus): Add option 5 for remove student
    print("5. Quit")
    print("=" * 34)


# ─── Main Function ────────────────────────────────────────────────────────────

def main():
    """
    Main gradebook loop.
    - Show the menu
    - Get user's choice
    - Call the appropriate function
    - Loop until quit
    """
    # Initialize the gradebook as an empty dictionary
    gradebook = {}

    print("Welcome to the Student Gradebook! 📚")

    while True:
        display_menu()

        # TODO: Get the user's menu choice
        choice = None  # Replace with: input("Choose option (1-5): ").strip()

        # TODO: Handle each menu option
        # if choice == "1":
        #     add_student(gradebook)
        # elif choice == "2":
        #     view_all_students(gradebook)
        # elif choice == "3":
        #     search_student(gradebook)
        # elif choice == "4":
        #     calculate_average(gradebook)
        # elif choice == "5":
        #     print("Goodbye! 👋")
        #     break
        # else:
        #     print("Invalid option. Please choose 1-5.")
        pass


if __name__ == "__main__":
    main()
