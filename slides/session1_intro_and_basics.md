---
marp: true
theme: default
paginate: true
---

# 🐍 Welcome to Python!
## Session 1: Introduction to Python & Programming Basics

**Duration:** 1 hour 40 minutes
**Your instructor is excited to meet you!**

---

# 📋 What We'll Cover Today

1. What is Python & why learn it?
2. Setting up your environment
3. Hello, World!
4. Variables & Data Types
5. Arithmetic & Assignment Operators
6. User Input with `input()`
7. Type Conversion
8. Comments & Code Readability
9. Live Coding & Practice

---

# 🌍 What is Python?

- A **general-purpose, high-level** programming language
- Created by **Guido van Rossum** in 1991
- Named after *Monty Python's Flying Circus* 🎭
- One of the **most popular** languages in the world

```
Timeline:
1991 ──► Python 1.0
1994 ──► Python 1.4
2000 ──► Python 2.0
2008 ──► Python 3.0
2023 ──► Python 3.12 (current)
```

---

# 🚀 What Can Python Do?

| Field | Examples |
|-------|---------|
| 🌐 Web Development | Instagram, Pinterest, Django |
| 🤖 AI & Machine Learning | TensorFlow, ChatGPT tools |
| 📊 Data Science | Pandas, NumPy, Jupyter |
| 🎮 Game Development | Pygame |
| 🔬 Science & Research | NASA, CERN |
| 🤖 Automation | Scripts, bots, task automation |

**Python is everywhere — and it's beginner-friendly!**

---

# 💻 Setting Up Your Environment

### Option 1: Local Install (Recommended)
1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Download Python 3.10 or newer
3. Install **VS Code** + Python extension

### Option 2: Online (Zero Setup)
- [Google Colab](https://colab.research.google.com) — free, in your browser
- [repl.it](https://replit.com) — online IDE

### Verify your installation:
```bash
python --version
# Should show: Python 3.10.x or higher
```

---

# 👋 Your First Python Program

Open your editor and type:

```python
print("Hello, World!")
```

Run it! You should see:
```
Hello, World!
```

**Congratulations — you're a programmer! 🎉**

### More `print` examples:
```python
print("My name is Alice")
print("2 + 2 =", 2 + 2)
print("Python is", "awesome!")
```

---

# 📦 Variables — Boxes That Hold Values

A **variable** is a named storage location for data.

```python
name = "Alice"         # str  — text
age = 25               # int  — whole number
height = 1.68          # float — decimal number
is_student = True      # bool — True or False
```

```
 ┌─────────┐    ┌─────────┐    ┌──────────┐
 │  name   │    │   age   │    │  height  │
 │ "Alice" │    │   25    │    │   1.68   │
 └─────────┘    └─────────┘    └──────────┘
```

### Rules for variable names:
- Start with a letter or `_` (not a number)
- No spaces — use `_` instead: `first_name`
- Case-sensitive: `age` ≠ `Age`

---

# 🔠 Data Types

```python
# Integer — whole numbers
score = 100
year = 2024

# Float — decimal numbers
price = 9.99
pi = 3.14159

# String — text (use quotes)
greeting = "Hello!"
city = 'Bucharest'

# Boolean — True or False
is_raining = False
passed_exam = True

# Check a type with type()
print(type(score))    # <class 'int'>
print(type(price))    # <class 'float'>
print(type(greeting)) # <class 'str'>
print(type(is_raining)) # <class 'bool'>
```

---

# ➕ Arithmetic Operators

```python
a = 10
b = 3

print(a + b)   # 13  — Addition
print(a - b)   # 7   — Subtraction
print(a * b)   # 30  — Multiplication
print(a / b)   # 3.333... — Division (always float)
print(a // b)  # 3   — Floor Division (whole number)
print(a % b)   # 1   — Modulo (remainder)
print(a ** b)  # 1000 — Exponentiation (10³)
```

### Order of Operations: PEMDAS/BODMAS
```python
result = 2 + 3 * 4    # 14 (not 20!)
result = (2 + 3) * 4  # 20
```

---

# 🔄 Assignment Operators

```python
x = 10          # Assign
x += 5          # x = x + 5  → 15
x -= 3          # x = x - 3  → 12
x *= 2          # x = x * 2  → 24
x /= 4          # x = x / 4  → 6.0
x //= 2         # x = x // 2 → 3.0
x **= 3         # x = x ** 3 → 27.0
```

### String operations:
```python
first = "Hello"
last = "World"
full = first + " " + last   # "Hello World"  — concatenation
repeated = "Ha" * 3          # "HaHaHa"      — repetition
```

---

# ⌨️ User Input with `input()`

`input()` pauses the program and waits for the user to type something.

```python
name = input("What is your name? ")
print("Hello,", name)
```

**Important:** `input()` always returns a **string**!

```python
age_str = input("How old are you? ")
print(type(age_str))  # <class 'str'>  ← NOT int!

# You need to convert it:
age = int(age_str)
print(type(age))      # <class 'int'>  ✓
```

---

# 🔁 Type Conversion

Convert between types using these built-in functions:

```python
# String to number
age = int("25")         # 25
price = float("9.99")   # 9.99

# Number to string
text = str(42)          # "42"
text = str(3.14)        # "3.14"

# In one line (common pattern):
age = int(input("Enter your age: "))
price = float(input("Enter price: "))

# Boolean conversions
bool(0)    # False
bool(1)    # True
bool("")   # False
bool("hi") # True
```

---

# 💬 Comments & Code Readability

Comments explain your code — they are ignored by Python.

```python
# This is a single-line comment

# Calculate the area of a rectangle
width = 5
height = 3
area = width * height   # multiply width by height
print(area)             # prints 15

# Multi-line comment (use multiple #):
# Step 1: Get user input
# Step 2: Do calculation
# Step 3: Display result
```

### Best practices:
- Write comments for *why*, not just *what*
- Use descriptive variable names: `user_age` not `x`
- Keep lines under ~79 characters

---

# 🧮 Putting It All Together

```python
# A simple "About Me" program

# Get user information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your favorite hobby: ")

# Calculate birth year
current_year = 2024
birth_year = current_year - age

# Display formatted output
print()
print("=== About Me ===")
print(f"Hi, I'm {name}!")
print(f"I'm {age} years old, born around {birth_year}.")
print(f"My favorite hobby is {hobby}.")
```

---

# 🎯 Practice Exercises

Try these on your own:

**Exercise 1:** Print your name and age using variables

**Exercise 2:** Calculate and print the area of a circle
- Get the radius from the user
- Use `pi = 3.14159`
- Area = π × r²

**Exercise 3:** Temperature converter
- Ask for temperature in Celsius
- Convert to Fahrenheit: `F = C × 9/5 + 32`
- Print the result

---

# 📝 Assignment 1: "About Me" Script

**Due:** Before Session 2

Write a Python script that:

1. Asks the user for their **name**, **age**, and **favorite hobby**
2. Calculates the **year they were born** (approximately)
3. Prints a formatted summary:
   > *"Hi, I'm Alice. I'm 25 years old, born around 2001, and I love hiking!"*

**⭐ Bonus:** Ask for two numbers and print their sum, difference, product, and quotient.

📁 Start with: `starter-code/assignment1_starter.py`
📄 Full details: `assignments/assignment1_about_me.md`

---

# 🎉 Session 1 Recap

Today you learned:

✅ What Python is and why it's awesome
✅ How to set up your coding environment
✅ `print()` — displaying output
✅ Variables and the 4 basic data types
✅ Arithmetic and assignment operators
✅ `input()` — getting user input
✅ Type conversion: `int()`, `float()`, `str()`
✅ Writing comments

**See you in Session 2! 🚀**
