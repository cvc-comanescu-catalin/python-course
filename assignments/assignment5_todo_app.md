# Assignment 5: To-Do List App ✅ (Final Project)

## 🎯 Objective

Build a complete command-line To-Do List application that persists data to a file. This final project integrates everything you've learned: functions, data structures, file I/O, error handling, and user input. **This is your capstone project!**

---

## 📋 Requirements

### Part 1 — Data Structure
Each task is represented as a dictionary:
```python
task = {
    "description": "Buy groceries",
    "done": False
}
```
All tasks are stored in a list: `tasks = [task1, task2, ...]`

### Part 2 — File Persistence
The app saves and loads tasks from a file (`tasks.txt` by default).

#### `load_tasks(filename)`:
- Opens the file and reads all tasks
- Returns a list of task dictionaries
- Handles `FileNotFoundError` — if the file doesn't exist, return an empty list

#### `save_tasks(tasks, filename)`:
- Writes all tasks to the file
- Each line: `description|done` (e.g., `Buy groceries|False`)

### Part 3 — Core Operations

#### `add_task(tasks)`:
- Asks for a task description
- Validates that the description is not empty
- Appends a new task dict to the list
- Prints confirmation

#### `view_tasks(tasks)`:
- If no tasks, prints `"No tasks yet! Add one above."`
- Otherwise, prints all tasks with index, status, and description:
  ```
  === Your Tasks ===
  1. [○] Buy groceries
  2. [✓] Study Python
  3. [○] Call dentist
  ```

#### `complete_task(tasks)`:
- Shows the task list (with numbers)
- Asks for the task number to mark complete
- Sets `task["done"] = True`
- Validates the number (must be a valid index)

#### `delete_task(tasks)`:
- Shows the task list
- Asks for the task number to delete
- Removes the task with `tasks.pop(index)`
- Validates the number

### Part 4 — Menu & Main Loop

```
============================
        ✅ To-Do App
============================
1. Add task
2. View tasks
3. Mark as complete
4. Delete task
5. Quit
============================
Choose an option (1-5):
```

The app should:
- Load tasks from file **on startup**
- Save tasks to file **whenever tasks change** (or at minimum, on quit)
- Loop until the user chooses "Quit"

---

## ⭐ Bonus / Stretch Goals

### Bonus 1 — Due Dates
Add a `due_date` field to each task. Ask for it when adding a task (or leave blank). Display it next to the task description.

### Bonus 2 — Priorities
Add a `priority` field: Low / Medium / High. Display tasks sorted by priority.

### Bonus 3 — Categories
Add a `category` field (e.g., Work, Personal, Shopping). Allow filtering tasks by category.

### Bonus 4 — Statistics
Add a menu option to show:
```
📊 Statistics:
Total tasks:     5
Completed:       2
Remaining:       3
Completion rate: 40%
```

### Bonus 5 — Search
Add a search feature that finds tasks whose description contains a keyword.

---

## 💡 Hints

- Load tasks at the very start of `main()`:
  ```python
  tasks = load_tasks(FILENAME)
  ```
- File format for each line: `description|done` e.g. `Buy milk|False`
- Parsing a line back into a dict:
  ```python
  parts = line.strip().split("|")
  task = {"description": parts[0], "done": parts[1] == "True"}
  ```
- Validate task number input:
  ```python
  try:
      index = int(input("Task number: ")) - 1  # Convert to 0-based
      if 0 <= index < len(tasks):
          # valid
      else:
          print("Invalid task number!")
  except ValueError:
      print("Please enter a number!")
  ```
- `"True" == "True"` is `True`, `"False" == "True"` is `False` — use this to parse the done field

---

## 📟 Example Session

```
============================
        ✅ To-Do App
============================
Loaded 0 tasks.

1. Add task
2. View tasks
3. Mark as complete
4. Delete task
5. Quit
============================
Choose an option (1-5): 1

Task description: Buy groceries
✓ Task added: "Buy groceries"

Choose an option (1-5): 1
Task description: Study Python
✓ Task added: "Study Python"

Choose an option (1-5): 2

=== Your Tasks ===
1. [○] Buy groceries
2. [○] Study Python

Choose an option (1-5): 3

=== Your Tasks ===
1. [○] Buy groceries
2. [○] Study Python
Mark task number as complete: 2
✓ Marked "Study Python" as complete!

Choose an option (1-5): 2

=== Your Tasks ===
1. [○] Buy groceries
2. [✓] Study Python

Choose an option (1-5): 5
Tasks saved. Goodbye! 👋
```

---

## ✅ Checklist

Before submitting, make sure your app:

- [ ] `load_tasks()` — reads tasks from file (handles missing file)
- [ ] `save_tasks()` — writes tasks to file in correct format
- [ ] `add_task()` — adds task with non-empty description check
- [ ] `view_tasks()` — displays tasks with number, status, description
- [ ] `complete_task()` — marks a task as done with valid index check
- [ ] `delete_task()` — removes a task with valid index check
- [ ] `display_menu()` — prints the menu
- [ ] `main()` — loads on startup, shows menu loop, saves on exit
- [ ] Uses `if __name__ == "__main__":` guard
- [ ] Handles all error cases gracefully

**Bonus:**
- [ ] Due dates
- [ ] Priority levels
- [ ] Categories with filter
- [ ] Statistics display
- [ ] Search by keyword

---

## 📤 Submission Instructions

1. Open `starter-code/assignment5_starter.py`
2. Fill in all the `TODO` sections — this is the most complex assignment!
3. Test your app thoroughly:
   - Add several tasks
   - Mark some complete
   - Delete one
   - Quit and restart — tasks should persist!
4. Save your completed file as `assignment5_yourname.py`
5. Submit via the course platform or share the GitHub link

---

## 🎓 Course Completion

By completing this assignment, you've built a **real, working application** that:
- Takes user input
- Uses data structures (lists of dicts)
- Reads and writes files
- Handles errors
- Has a clean, user-friendly interface

**Congratulations on completing the Python for Beginners course! 🎉🐍**

---

*💡 Tip: Build it step by step. Get Part 2 (file I/O) working before building the UI!*
