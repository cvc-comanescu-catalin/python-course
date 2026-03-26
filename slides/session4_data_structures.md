---
marp: true
theme: default
paginate: true
---

# 📦 Data Structures
## Session 4: Lists, Tuples & Dictionaries

**Duration:** 1 hour 40 minutes

---

# 📋 What We'll Cover Today

1. Recap & Assignment 3 Review
2. Lists: creation, indexing, slicing, methods
3. Looping through lists
4. List comprehensions (intro)
5. Tuples — immutable sequences
6. Dictionaries: key-value pairs, methods
7. Nested data structures
8. Practice

---

# 🧠 Recap & Assignment 3 Review

Quick check:

```python
# What does this print?
def mystery(x, y=10):
    return x * y

print(mystery(3))
print(mystery(3, 5))

# What's the scope issue here?
def double():
    result = x * 2   # Is this okay?

x = 5
double()
```

---

# 📋 Lists — Ordered Collections

A list is an **ordered, changeable** collection of items.

```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [42, "hello", True, 3.14]
empty = []

# Indexing — starts at 0!
#   Index:  0        1         2
fruits = ["apple", "banana", "cherry"]

print(fruits[0])    # "apple"
print(fruits[1])    # "banana"
print(fruits[-1])   # "cherry"  ← negative index from end
print(fruits[-2])   # "banana"
```

---

# ✂️ List Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [start:stop]  — stop is NOT included
print(numbers[2:5])    # [2, 3, 4]
print(numbers[:4])     # [0, 1, 2, 3]  — from beginning
print(numbers[6:])     # [6, 7, 8, 9]  — to end
print(numbers[:])      # [0, 1, 2, ... 9]  — full copy

# [start:stop:step]
print(numbers[::2])    # [0, 2, 4, 6, 8]  — every 2nd
print(numbers[::-1])   # [9, 8, 7, ... 0]  — reversed!

# Visual:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#  ↑                 ↑
# [2:5] → takes index 2, 3, 4 → [2, 3, 4]
```

---

# 🛠️ Common List Methods

```python
fruits = ["apple", "banana"]

# Adding items
fruits.append("cherry")        # Add to end → [..., "cherry"]
fruits.insert(1, "blueberry")  # Insert at index 1

# Removing items
fruits.remove("banana")        # Remove by value
last = fruits.pop()            # Remove & return last item
item = fruits.pop(0)           # Remove & return at index 0

# Other useful methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()                 # Sort in place → [1, 1, 2, 3, 4, 5, 6, 9]
numbers.reverse()              # Reverse in place
print(len(numbers))            # 8
print(numbers.count(1))        # 2 — how many times 1 appears
print(numbers.index(5))        # 4 — index of value 5
```

---

# 🔁 Looping Through Lists

```python
fruits = ["apple", "banana", "cherry", "date"]

# Simple loop
for fruit in fruits:
    print(fruit)

# Loop with index using enumerate()
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Loop and modify (use range + len)
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)   # [2, 4, 6, 8, 10]
```

---

# ✨ List Comprehensions

A concise way to create or transform lists:

```python
# Traditional way:
squares = []
for n in range(1, 6):
    squares.append(n ** 2)

# List comprehension — same result in one line!
squares = [n ** 2 for n in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# With a condition (filter):
evens = [n for n in range(20) if n % 2 == 0]
print(evens)     # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transform strings:
words = ["hello", "world", "python"]
upper = [word.upper() for word in words]
print(upper)     # ['HELLO', 'WORLD', 'PYTHON']
```

---

# 🔒 Tuples — Immutable Sequences

Tuples are like lists, but **cannot be changed** after creation.

```python
# Creating tuples (use parentheses)
point = (3, 7)
rgb = (255, 128, 0)
single = (42,)   # ← Note the comma! (42) is just an int

# Accessing elements — same as lists
print(point[0])   # 3
print(rgb[-1])    # 0

# Unpacking
x, y = point
print(f"x={x}, y={y}")   # x=3, y=7

lat, lon = 44.4268, 26.1025   # Bucharest coordinates
```

### When to use tuples vs. lists:
- **Tuple**: Fixed data (coordinates, RGB, days of week)
- **List**: Data that will change (shopping cart, user list)

---

# 📖 Dictionaries — Key-Value Pairs

```python
# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics"]
}

# Accessing values
print(student["name"])      # "Alice"
print(student.get("age"))   # 20
print(student.get("gpa", 0.0))  # 0.0 (default if key missing)

# Adding / updating
student["email"] = "alice@example.com"  # Add new key
student["age"] = 21                     # Update existing key

# Deleting
del student["grade"]
removed = student.pop("age")
```

---

# 🔍 Dictionary Methods

```python
person = {"name": "Bob", "age": 30, "city": "Paris"}

# Keys, values, items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Bob', 30, 'Paris'])
print(person.items())   # dict_items([('name', 'Bob'), ...])

# Looping
for key in person:
    print(key, "→", person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Check if key exists
if "name" in person:
    print("Name is:", person["name"])
```

---

# 🏗️ Nested Data Structures

Combine lists and dicts for complex data:

```python
# List of dictionaries (common pattern!)
students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob",   "grade": 85},
    {"name": "Carol", "grade": 97},
]

# Access nested data
print(students[0]["name"])   # "Alice"
print(students[2]["grade"])  # 97

# Loop through list of dicts
for student in students:
    print(f"{student['name']}: {student['grade']}")

# Dictionary of lists
gradebook = {
    "Alice": [90, 85, 92],
    "Bob":   [78, 82, 80],
}
print(sum(gradebook["Alice"]) / len(gradebook["Alice"]))  # Average
```

---

# 🎯 Practice Exercises

**Exercise 1:** Create a list of 5 of your favorite movies. Print them numbered (1. Movie Name).

**Exercise 2:** Use a list comprehension to create a list of all numbers divisible by 3 between 1 and 50.

**Exercise 3:** Create a dictionary for a contact (name, phone, email, city). Print each field on its own line.

**Exercise 4:** Given `scores = [78, 92, 85, 90, 88, 76]`, calculate the average without using `sum()` (use a loop).

**Exercise 5:** Write a function `most_common(lst)` that returns the most frequent item in a list.

---

# 📝 Assignment 4: Student Gradebook

**Due:** Before Session 5

Create a program that:

1. Stores student names and their grades in a **dictionary**
2. Lets the user: **add** a student, **view** all students, **look up** a student's grade, **calculate** the class average
3. Uses a **menu-driven loop**
4. **Validates** user input (what if the student doesn't exist?)

**⭐ Bonus:**
- Store **multiple grades** per student (dict of lists)
- Find **highest/lowest** scoring student
- Show a grade distribution (A/B/C/D/F count)
- Allow removing a student

📁 Start with: `starter-code/assignment4_starter.py`
📄 Full details: `assignments/assignment4_gradebook.md`

---

# 🎉 Session 4 Recap

Today you learned:

✅ Lists: creation, indexing, slicing, methods
✅ Looping through lists with `for` and `enumerate()`
✅ List comprehensions for concise list creation
✅ Tuples: immutable, use for fixed data
✅ Dictionaries: key-value pairs, CRUD operations
✅ Iterating dicts with `.keys()`, `.values()`, `.items()`
✅ Nested structures: list of dicts, dict of lists

**See you in Session 5 — the final session! 🚀**
