---
marp: true
theme: default
paginate: true
---

# 📁 Files, Errors & Your First Project
## Session 5: File I/O, Error Handling & Mini-Project

**Duration:** 1 hour 40 minutes

---

# 📋 What We'll Cover Today

1. Recap & Assignment 4 Review
2. Reading files: `open()`, `read()`, `readlines()`, `with`
3. Writing & Appending files
4. Error handling: `try`, `except`, `finally`
5. Common Exceptions
6. f-strings deep dive
7. 🎓 Course recap
8. 🛠️ Mini-Project: Command-Line To-Do App

---

# 🧠 Recap & Assignment 4 Review

Quick check:

```python
# What's the output?
data = {"a": 1, "b": 2, "c": 3}
result = [k for k, v in data.items() if v > 1]
print(result)

# Fix the bug:
students = [{"name": "Alice", "grade": 90}]
for s in students:
    print(s[name])   # Error — what's wrong?

# What does this create?
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
```

---

# 📂 Reading Files

```python
# Basic file reading
file = open("data.txt", "r")   # "r" = read mode
content = file.read()          # Read entire file as string
print(content)
file.close()                   # Always close!

# Better way — with statement (auto-closes)
with open("data.txt", "r") as file:
    content = file.read()
# File is automatically closed here ✓

# Read line by line
with open("data.txt", "r") as file:
    lines = file.readlines()   # Returns list of strings
    for line in lines:
        print(line.strip())    # .strip() removes \n
```

---

# 📂 File Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read (default) — file must exist |
| `"w"` | Write — creates new or overwrites |
| `"a"` | Append — adds to end of file |
| `"r+"` | Read and write |
| `"rb"` | Read binary (images, etc.) |

```python
# Reading line by line (memory efficient for large files)
with open("big_file.txt", "r") as file:
    for line in file:           # Iterate directly!
        print(line.strip())

# Read and process each line
with open("names.txt", "r") as file:
    names = [line.strip() for line in file]
print(names)
```

---

# ✏️ Writing & Appending Files

```python
# Write mode — creates new file (or overwrites!)
with open("output.txt", "w") as file:
    file.write("Hello, File!\n")
    file.write("Second line\n")

# Write multiple lines at once
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Append mode — adds to existing file
with open("log.txt", "a") as file:
    file.write("New log entry\n")

# Write structured data
tasks = ["Buy milk", "Call mom", "Study Python"]
with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")
```

---

# 🛡️ Error Handling: try / except

Python raises **exceptions** when something goes wrong.

```python
# Without error handling — program crashes!
age = int(input("Enter age: "))  # What if user types "abc"?

# With error handling — graceful!
try:
    age = int(input("Enter age: "))
    print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid number!")

# The flow:
# try block runs
# If an error occurs → jump to except
# If no error → skip except
# Program continues either way ✓
```

---

# 🛡️ More Error Handling Patterns

```python
# Catch multiple exception types
try:
    result = int(input("Number: ")) / int(input("Divide by: "))
    print(f"Result: {result}")
except ValueError:
    print("Please enter valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# finally — always runs (great for cleanup)
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
    content = ""
finally:
    print("Done attempting to read file.")
```

---

# ⚠️ Common Exceptions

| Exception | When it occurs |
|-----------|---------------|
| `ValueError` | Wrong type: `int("abc")` |
| `ZeroDivisionError` | Dividing by zero: `10 / 0` |
| `FileNotFoundError` | File doesn't exist |
| `IndexError` | List index out of range: `lst[99]` |
| `KeyError` | Dict key missing: `d["missing"]` |
| `TypeError` | Wrong operation: `"hi" + 5` |
| `NameError` | Variable not defined: `print(x)` |

```python
# Catching any exception (use sparingly!)
try:
    risky_operation()
except Exception as e:
    print(f"An error occurred: {e}")
```

---

# 🎨 f-strings Deep Dive

```python
name = "Alice"
score = 95.678
balance = 1234567.89

# Basic
print(f"Hello, {name}!")

# Expressions inside {}
print(f"Score: {score:.2f}")       # 95.68 (2 decimal places)
print(f"Score: {score:.0f}")       # 96 (no decimals)
print(f"Name: {name:>10}")         # right-align in 10 chars
print(f"Name: {name:<10}|")        # left-align
print(f"Name: {name:^10}")         # center

# Numbers
print(f"Balance: {balance:,.2f}")  # 1,234,567.89 (with commas)
print(f"Pi: {3.14159:.3f}")        # 3.142

# Expressions
print(f"Double: {score * 2}")
print(f"Upper: {name.upper()}")
```

---

# 🎓 Course Recap — Everything You've Learned!

```
Session 1  ──►  print(), variables, data types, input(), operators
                          │
Session 2  ──►  if/elif/else, while, for, range, break, continue
                          │
Session 3  ──►  def, parameters, return, scope, modules
                          │
Session 4  ──►  lists, tuples, dicts, comprehensions
                          │
Session 5  ──►  file I/O, try/except, f-strings
```

**You can now build real programs that:**
- Take user input and make decisions
- Repeat actions efficiently
- Organize code into reusable functions
- Work with complex data
- Read/write files and handle errors

---

# 🛠️ Mini-Project: To-Do App — Step 1: Design

We'll build a **Command-Line To-Do App** together!

Features:
1. Add tasks
2. View all tasks
3. Mark task as complete
4. Delete a task
5. Save to file (tasks persist!)
6. Load on startup

```
=== To-Do App ===
1. Add task
2. View tasks
3. Mark complete
4. Delete task
5. Quit

Choose an option: _
```

---

# 🛠️ Mini-Project — Step 2: Data Structure

```python
FILENAME = "tasks.txt"

# Each task is a dict:
task = {
    "description": "Buy groceries",
    "done": False
}

# All tasks in a list:
tasks = [
    {"description": "Buy groceries", "done": False},
    {"description": "Study Python",  "done": True},
]
```

---

# 🛠️ Mini-Project — Step 3: Core Functions

```python
def load_tasks():
    tasks = []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                tasks.append({
                    "description": parts[0],
                    "done": parts[1] == "True"
                })
    except FileNotFoundError:
        pass   # No file yet — start fresh
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(f"{task['description']}|{task['done']}\n")
```

---

# 🛠️ Mini-Project — Step 4: UI Functions

```python
def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    print("\n=== Your Tasks ===")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "○"
        print(f"{i}. [{status}] {task['description']}")

def add_task(tasks):
    desc = input("Task description: ").strip()
    if desc:
        tasks.append({"description": desc, "done": False})
        print(f"Added: '{desc}'")
    else:
        print("Task cannot be empty!")
```

---

# 🎯 Practice Exercises

**Exercise 1:** Write a function that reads a file and counts the number of lines, words, and characters.

**Exercise 2:** Write a try/except block that:
- Opens a file the user specifies
- Handles `FileNotFoundError` gracefully
- Prints the first 5 lines

**Exercise 3:** Extend the To-Do App to support a "search tasks" feature.

---

# 📝 Assignment 5: To-Do List App (Final Project)

Build a **complete** To-Do List App that:

1. Lets the user **add**, **view**, **mark complete**, **delete** tasks
2. **Saves** tasks to a text file (persists between runs!)
3. **Loads** tasks from the file on startup
4. Uses **functions** for each operation
5. **Handles errors** gracefully

**⭐ Bonus:** Add due dates, priority levels, or categories.

📁 Start with: `starter-code/assignment5_starter.py`
📄 Full details: `assignments/assignment5_todo_app.md`

---

# 🚀 What's Next After This Course?

### Intermediate Topics to Explore:
- **Classes & OOP** — `class`, objects, inheritance
- **List/dict comprehensions** — advanced patterns
- **Decorators & generators** — powerful Python features
- **Virtual environments** — `venv`, pip
- **Popular libraries**: `requests`, `pandas`, `flask`

### Project Ideas:
- Web scraper with `requests` + `BeautifulSoup`
- Simple web app with `Flask`
- Data analysis with `pandas`
- Discord/Telegram bot

### Resources:
- [Real Python](https://realpython.com) | [Python Docs](https://docs.python.org/3/) | [Automate the Boring Stuff](https://automatetheboringstuff.com/)

---

# 🎉 Congratulations!

You've completed the **Python for Beginners** course!

### You now know how to:
✅ Write and run Python programs
✅ Use variables, data types, and operators
✅ Control program flow with conditions and loops
✅ Write reusable functions
✅ Work with lists, tuples, and dictionaries
✅ Read and write files
✅ Handle errors gracefully
✅ Build a complete command-line application

**Keep coding, keep learning! 🐍**
