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
  Each line: description|done|due_date|priority|category
  Example:   Buy groceries|False|2026-06-01|High|Shopping
             Study Python|True|||
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

    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) >= 2:
                    tasks.append({
                        "description": parts[0],
                        "done": parts[1] == "True",
                        "due_date": parts[2] if len(parts) > 2 else "",
                        "priority": parts[3] if len(parts) > 3 and parts[3] else "Medium",
                        "category": parts[4] if len(parts) > 4 else "",
                    })
    except FileNotFoundError:
        pass  # No file yet — start with an empty list

    return tasks


def save_tasks(tasks, filename=FILENAME):
    """
    Save all tasks to a file, overwriting any existing content.
    Each line: description|done

    Parameters:
        tasks    (list): List of task dicts to save
        filename (str):  Path to the file
    """
    with open(filename, "w") as f:
        for task in tasks:
            f.write(
                f"{task['description']}|"
                f"{task['done']}|"
                f"{task.get('due_date', '')}|"
                f"{task.get('priority', 'Medium')}|"
                f"{task.get('category', '')}\n"
            )


# ─── Task Operations ──────────────────────────────────────────────────────────

def add_task(tasks):
    """
    Ask the user for a task description and add it to the tasks list.
    The task starts as not done (done=False).
    Validate that the description is not empty.

    Parameters:
        tasks (list): The list to add the new task to (modified in place)
    """
    description = input("Task description: ").strip()
    if not description:
        print("Task description cannot be empty!")
        return

    due_date = input("Due date (YYYY-MM-DD, or leave blank): ").strip()

    print("Priority: 1. Low  2. Medium  3. High")
    priority_map = {"1": "Low", "2": "Medium", "3": "High"}
    priority = priority_map.get(input("Choose priority (1-3, default 2): ").strip(), "Medium")

    category = input("Category (e.g. Work, Personal, Shopping, or leave blank): ").strip()

    tasks.append({
        "description": description,
        "done": False,
        "due_date": due_date,
        "priority": priority,
        "category": category,
    })
    print(f'✓ Task added: "{description}"')


def view_tasks(tasks):
    """
    Display all tasks with their number, completion status, and description.
    If there are no tasks, print "No tasks yet! Add one."

    Parameters:
        tasks (list): List of task dicts to display
    """
    if not tasks:
        print("No tasks yet! Add one.")
        return

    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    sorted_tasks = sorted(
        enumerate(tasks, 1),
        key=lambda x: priority_order.get(x[1].get("priority", "Medium"), 2)
    )

    print("\n=== Your Tasks ===")
    for orig_i, task in sorted_tasks:
        status = "✓" if task["done"] else "○"
        priority = task.get("priority", "Medium")
        category = f" ({task['category']})" if task.get("category") else ""
        due = f" | Due: {task['due_date']}" if task.get("due_date") else ""
        print(f"{orig_i}. [{status}] [{priority}] {task['description']}{category}{due}")


def complete_task(tasks):
    """
    Ask the user which task to mark as complete, then update it.
    Validate the task number.

    Parameters:
        tasks (list): The list of tasks (modified in place)
    """
    view_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Mark task number as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f'✓ Marked "{tasks[index]["description"]}" as complete!')
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    """
    Ask the user which task to delete, then remove it from the list.
    Validate the task number.

    Parameters:
        tasks (list): The list of tasks (modified in place)
    """
    view_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Delete task number: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f'🗑️  Deleted "{removed["description"]}"')
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")


def show_statistics(tasks):
    """Display task statistics: totals, completion rate, and priority breakdown."""
    total = len(tasks)
    if total == 0:
        print("No tasks yet!")
        return

    completed = sum(1 for t in tasks if t["done"])
    remaining = total - completed
    rate = (completed / total) * 100

    print("\n📊 Statistics:")
    print(f"  Total tasks:     {total}")
    print(f"  Completed:       {completed}")
    print(f"  Remaining:       {remaining}")
    print(f"  Completion rate: {rate:.0f}%")

    print("\n  By priority:")
    for p in ["High", "Medium", "Low"]:
        count = sum(1 for t in tasks if t.get("priority") == p)
        print(f"    {p:<8} {count}")


def filter_by_category(tasks):
    """Show tasks belonging to a chosen category."""
    if not tasks:
        print("No tasks yet!")
        return

    categories = sorted(set(t.get("category", "") for t in tasks if t.get("category")))
    if not categories:
        print("No categories assigned yet.")
        return

    print("\nAvailable categories: " + ", ".join(categories))
    keyword = input("Filter by category: ").strip()
    if not keyword:
        return

    results = [(i, t) for i, t in enumerate(tasks, 1)
               if t.get("category", "").lower() == keyword.lower()]

    if not results:
        print(f'No tasks in category "{keyword}".')
        return

    print(f"\n=== Tasks in '{keyword}' ===")
    for orig_i, task in results:
        status = "✓" if task["done"] else "○"
        priority = task.get("priority", "Medium")
        due = f" | Due: {task['due_date']}" if task.get("due_date") else ""
        print(f"{orig_i}. [{status}] [{priority}] {task['description']}{due}")


def search_tasks(tasks):
    """Find tasks whose description contains a keyword."""
    if not tasks:
        print("No tasks yet!")
        return

    keyword = input("Search keyword: ").strip().lower()
    if not keyword:
        print("Please enter a keyword.")
        return

    results = [(i, t) for i, t in enumerate(tasks, 1)
               if keyword in t["description"].lower()]

    if not results:
        print(f'No tasks found matching "{keyword}".')
        return

    print(f"\n=== Search results for '{keyword}' ===")
    for orig_i, task in results:
        status = "✓" if task["done"] else "○"
        priority = task.get("priority", "Medium")
        category = f" ({task['category']})" if task.get("category") else ""
        due = f" | Due: {task['due_date']}" if task.get("due_date") else ""
        print(f"{orig_i}. [{status}] [{priority}] {task['description']}{category}{due}")


def display_menu():
    """Print the To-Do App menu."""
    print("\n" + "=" * 28)
    print("        ✅ To-Do App")
    print("=" * 28)
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark as complete")
    print("4. Delete task")
    print("5. Statistics")
    print("6. Filter by category")
    print("7. Search tasks")
    print("8. Quit")
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
    tasks = load_tasks()
    print(f"Loaded {len(tasks)} task(s).")

    # Step 2: Main loop
    while True:
        display_menu()

        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            show_statistics(tasks)
        elif choice == "6":
            filter_by_category(tasks)
        elif choice == "7":
            search_tasks(tasks)
        elif choice == "8":
            save_tasks(tasks)
            print("Tasks saved. Goodbye! 👋")
            break
        else:
            print("Invalid option. Please choose 1-8.")


if __name__ == "__main__":
    main()
