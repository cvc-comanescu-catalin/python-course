---
marp: true
theme: default
paginate: true
---

# 🔧 Functions & Modular Thinking
## Session 3: Writing Reusable Code

**Duration:** 1 hour 40 minutes

---

# 📋 What We'll Cover Today

1. Recap & Assignment 2 Review
2. Why Functions? The DRY Principle
3. Defining Functions: `def`, parameters, `return`
4. Default Parameters & Keyword Arguments
5. Variable Scope: local vs. global
6. Built-in Functions Cheat Sheet
7. Importing Modules: `math`, `random`
8. Practice

---

# 🧠 Recap & Assignment 2 Review

Quick check:

```python
# What does this output?
for i in range(3, 10, 3):
    print(i)

# What does this do?
count = 0
while count < 5:
    if count == 3:
        break
    count += 1
print(count)

# Fix the bug:
numbers = "12345"
for n in numbers:
    print(n * 2)    # What's the issue?
```

---

# 🤔 Why Functions? The DRY Principle

**DRY = Don't Repeat Yourself**

❌ Without functions — repetitive:
```python
print("=" * 30)
print("  Welcome to the Game!")
print("=" * 30)
# ... lots of code ...
print("=" * 30)
print("  Game Over!")
print("=" * 30)
```

✅ With functions — clean:
```python
def print_banner(message):
    print("=" * 30)
    print(f"  {message}")
    print("=" * 30)

print_banner("Welcome to the Game!")
# ... lots of code ...
print_banner("Game Over!")
```

---

# 🔧 Anatomy of a Function

```python
#   keyword  name      parameters
#     ↓       ↓          ↓
def greet(name, greeting="Hello"):
    """This is a docstring — explains what the function does."""
    message = f"{greeting}, {name}!"   # function body
    return message                      # return value
#      ↑
#  return keyword

# Calling the function:
result = greet("Alice")
print(result)           # Hello, Alice!

result2 = greet("Bob", "Hi")
print(result2)          # Hi, Bob!
```

---

# 📥 Parameters vs. Arguments

```python
def add(a, b):       # a and b are PARAMETERS (in definition)
    return a + b

result = add(3, 5)   # 3 and 5 are ARGUMENTS (in call)
```

### Multiple parameters:
```python
def describe_pet(name, animal_type, age):
    print(f"{name} is a {age}-year-old {animal_type}.")

describe_pet("Rex", "dog", 3)
# Rex is a 3-year-old dog.

# What if the function has no return?
def say_hi(name):
    print(f"Hi {name}!")
    # implicitly returns None

value = say_hi("Alice")
print(value)   # None
```

---

# ⚙️ Default Parameters & Keyword Arguments

```python
# Default parameters — used if argument is not provided
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9  — uses default exponent=2
print(power(3, 3))   # 27 — overrides default

# Keyword arguments — order doesn't matter
def create_profile(name, age, city="Unknown"):
    print(f"{name}, {age}, from {city}")

create_profile("Alice", 25)
create_profile(age=30, name="Bob", city="Paris")
create_profile("Carol", city="Tokyo", age=22)
```

---

# 🔭 Variable Scope: Local vs. Global

```python
total = 0   # Global variable — accessible everywhere

def add_to_total(amount):
    global total          # Declare we're using the global
    total += amount       # Modify global variable

def calculate():
    result = 100          # Local variable — only inside this function
    print(result)

calculate()
# print(result)  ← ERROR! result is local to calculate()

add_to_total(50)
print(total)   # 50
```

### Best practice: avoid `global` — return values instead!
```python
def add(a, b):
    return a + b          # Return instead of using global

total = add(10, 20)      # Assign the returned value
```

---

# 📚 Built-in Functions Cheat Sheet

```python
# Math
abs(-5)           # 5      — absolute value
round(3.7)        # 4      — round to nearest int
round(3.14159, 2) # 3.14   — round to 2 decimal places
max(1, 5, 3)      # 5      — maximum
min(1, 5, 3)      # 1      — minimum
sum([1, 2, 3])    # 6      — sum of list

# Type & Info
type("hello")     # <class 'str'>
len("Python")     # 6      — length
len([1, 2, 3])    # 3

# Conversion
int("42")         # 42
float("3.14")     # 3.14
str(100)          # "100"
bool(0)           # False
list("abc")       # ['a', 'b', 'c']
```

---

# 📦 Importing Modules

```python
# Import the whole module
import math

print(math.pi)           # 3.141592653589793
print(math.sqrt(16))     # 4.0
print(math.floor(3.7))   # 3
print(math.ceil(3.2))    # 4
print(math.factorial(5)) # 120

# Import specific things
from random import randint, choice, shuffle

number = randint(1, 10)   # Random int between 1 and 10
item = choice(["a", "b", "c"])  # Random item from list
```

---

# 🎲 The `random` Module

```python
import random

# Random integer
random.randint(1, 6)       # Simulates a dice roll: 1-6

# Random float between 0 and 1
random.random()            # e.g., 0.7234

# Random choice from a sequence
fruits = ["apple", "banana", "cherry"]
random.choice(fruits)      # e.g., "banana"

# Shuffle a list (modifies in place)
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)      # e.g., [3, 1, 5, 2, 4]

# Sample without replacement
random.sample(range(50), 6)  # Pick 6 lottery numbers
```

---

# 🧩 Functions Calling Functions

```python
def square(n):
    return n ** 2

def sum_of_squares(a, b):
    return square(a) + square(b)   # calls square() twice

print(sum_of_squares(3, 4))  # 9 + 16 = 25

# A complete example
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def temperature_report(city, temp_c):
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{city}: {temp_c}°C = {temp_f:.1f}°F")

temperature_report("Bucharest", 25)  # Bucharest: 25°C = 77.0°F
temperature_report("London", 15)     # London: 15°C = 59.0°F
```

---

# 🎯 Practice Exercises

**Exercise 1:** Write a function `is_even(n)` that returns `True` if n is even.

**Exercise 2:** Write a function `celsius_to_kelvin(c)` that converts Celsius to Kelvin. (K = C + 273.15)

**Exercise 3:** Write a function `count_vowels(text)` that counts how many vowels are in a string.

**Exercise 4:** Write a function `roll_dice(sides=6)` that simulates rolling a dice with a given number of sides (default: 6).

**Exercise 5:** Write a function `bmi(weight_kg, height_m)` that calculates Body Mass Index: weight / height².

---

# 📝 Assignment 3: Calculator with Functions

**Due:** Before Session 4

Build a command-line calculator that:

1. Has separate functions: `add()`, `subtract()`, `multiply()`, `divide()`
2. Shows a **menu** to the user and asks them to pick an operation
3. Handles **division by zero** gracefully
4. **Loops** until the user types "quit"

**⭐ Bonus:**
- Add `power()` and `square_root()` functions using the `math` module
- Add a history of calculations

📁 Start with: `starter-code/assignment3_starter.py`
📄 Full details: `assignments/assignment3_calculator.md`

---

# 🎉 Session 3 Recap

Today you learned:

✅ Why functions make code better (DRY principle)
✅ Defining functions with `def`
✅ Parameters, arguments, and `return`
✅ Default parameters & keyword arguments
✅ Local vs. global scope
✅ Useful built-in functions
✅ Importing and using `math` and `random`

**See you in Session 4! 🚀**
