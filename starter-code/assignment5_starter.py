"""
Assignment 5: To-Do List App (Final Project)
=============================================
Build a complete command-line To-Do List application with file persistence.

Topics practiced:
- File I/O (read, write, append)
- Error handling (try/except)
- Lists of dictionaries
- Functions
- f-strings
- Complete application design

Data format in file (tasks.txt):
  Each line: description|done
  Example:   Buy groceries|False
             Study Python|True
"""


# ─── Constants ────────────────────────────────────────────────────────────────

FILENAME = "tasks.txt"


# ─── File I/O Functions ───────────────────────────────────────────────────────

def load_tasks(filename=FILENAME):
    """
    Load tasks from a file and return them as a list of dicts.
    If the file doesn't exist, return an empty list (do NOT crash!).

    Returns:
        list: A list of task dicts, e.g.:
              [{"description": "Buy milk", "done": False}, ...]
    """
    tasks = []

    # TODO: Use try/except to handle FileNotFoundError
    # Open the file, read each line, parse it into a dict, and append to tasks
    #
    # Hint:
    # try:
    #     with open(filename, "r") as f:
    #         for line in f:
    #             parts = line.strip().split("|")
    #             if len(parts) == 2:
    #                 tasks.append({
    #                     "description": parts[0],
    #                     "done": parts[1] == "True"
    #                 })
    # except FileNotFoundError:
    #     pass  # No file yet — start with an empty list

    return tasks


def save_tasks(tasks, filename=FILENAME):
    """
    Save all tasks to a file, overwriting any existing content.
    Each line: description|done

    Parameters:
        tasks    (list): List of task dicts to save
        filename (str):  Path to the file
    """
    # TODO: Open the file in write mode and write each task as a line
    # Hint:
    # with open(filename, "w") as f:
    #     for task in tasks:
    #         f.write(f"{task['description']}|{task['done']}\n")
    pass


# ─── Task Operations ──────────────────────────────────────────────────────────

def add_task(tasks):
    """
    Ask the user for a task description and add it to the tasks list.
    The task starts as not done (done=False).
    Validate that the description is not empty.

    Parameters:
        tasks (list): The list to add the new task to (modified in place)
    """
    # TODO: Ask for the task description
    description = None  # Replace with: input("Task description: ").strip()

    # TODO: Check it's not empty
    # If not empty: create a dict and append it to tasks, print confirmation
    # If empty: print "Task description cannot be empty!"
    pass


def view_tasks(tasks):
    """
    Display all tasks with their number, completion status, and description.
    If there are no tasks, print "No tasks yet! Add one."

    Parameters:
        tasks (list): List of task dicts to display
    """
    # TODO: Check if tasks is empty

    # TODO: Print a header

    # TODO: Loop with enumerate to print each task
    # Hint:
    # for i, task in enumerate(tasks, 1):
    #     status = "✓" if task["done"] else "○"
    #     print(f"{i}. [{status}] {task['description']}")
    pass


def complete_task(tasks):
    """
    Ask the user which task to mark as complete, then update it.
    Validate the task number.

    Parameters:
        tasks (list): The list of tasks (modified in place)
    """
    # TODO: Show the current tasks first (call view_tasks)

    # TODO: Ask for the task number to mark complete
    # Convert to integer and adjust to 0-based index (subtract 1)

    # TODO: Validate the index is within range, then set task["done"] = True
    # Hint:
    # try:
    #     index = int(input("Mark task number as complete: ")) - 1
    #     if 0 <= index < len(tasks):
    #         tasks[index]["done"] = True
    #         print(f'✓ Marked "{tasks[index]["description"]}" as complete!')
    #     else:
    #         print("Invalid task number!")
    # except ValueError:
    #     print("Please enter a valid number.")
    pass


def delete_task(tasks):
    """
    Ask the user which task to delete, then remove it from the list.
    Validate the task number.

    Parameters:
        tasks (list): The list of tasks (modified in place)
    """
    # TODO: Show the current tasks first

    # TODO: Ask for the task number to delete

    # TODO: Validate the index and remove the task using tasks.pop(index)
    # Print a confirmation message
    pass


def display_menu():
    """Print the To-Do App menu."""
    print("\n" + "=" * 28)
    print("        ✅ To-Do App")
    print("=" * 28)
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark as complete")
    print("4. Delete task")
    print("5. Quit")
    print("=" * 28)


# ─── Main Function ────────────────────────────────────────────────────────────

def main():
    """
    Main application loop.
    1. Load tasks from file on startup
    2. Show menu and handle user choices
    3. Save tasks whenever they change (or at least on quit)
    """
    print("🗒️  Welcome to the To-Do App!")

    # Step 1: Load existing tasks from file
    # TODO: Call load_tasks() and store the result
    tasks = []  # Replace with: tasks = load_tasks()
    print(f"Loaded {len(tasks)} task(s).")

    # Step 2: Main loop
    while True:
        display_menu()

        # TODO: Get user's menu choice
        choice = None  # Replace with: input("Choose an option (1-5): ").strip()

        # TODO: Handle each choice
        # if choice == "1":
        #     add_task(tasks)
        #     save_tasks(tasks)   # Save after every change
        # elif choice == "2":
        #     view_tasks(tasks)
        # elif choice == "3":
        #     complete_task(tasks)
        #     save_tasks(tasks)
        # elif choice == "4":
        #     delete_task(tasks)
        #     save_tasks(tasks)
        # elif choice == "5":
        #     save_tasks(tasks)
        #     print("Tasks saved. Goodbye! 👋")
        #     break
        # else:
        #     print("Invalid option. Please choose 1-5.")
        pass


if __name__ == "__main__":
    main()
