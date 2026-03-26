---
marp: true
theme: default
paginate: true
---

# 🔀 Control Flow
## Session 2: Making Decisions & Repeating Actions

**Duration:** 1 hour 40 minutes

---

# 📋 What We'll Cover Today

1. Quick Recap Quiz
2. Comparison Operators
3. `if`, `elif`, `else` statements
4. Logical Operators: `and`, `or`, `not`
5. `while` loops
6. `for` loops & `range()`
7. `break` and `continue`
8. Live Coding: FizzBuzz & Guessing Game

---

# 🧠 Quick Recap Quiz

Answer these in your head (or type them out!):

1. What does `type("hello")` return?
2. What is the result of `10 % 3`?
3. What does `input()` always return?
4. Fix this code:
   ```python
   age = input("Your age: ")
   next_year = age + 1   # ← This crashes! Why?
   ```

---

# ⚖️ Comparison Operators

These return `True` or `False`:

```python
x = 10
y = 5

print(x == y)   # False  — Equal to
print(x != y)   # True   — Not equal to
print(x > y)    # True   — Greater than
print(x < y)    # False  — Less than
print(x >= 10)  # True   — Greater than or equal
print(x <= 9)   # False  — Less than or equal
```

```python
# Works with strings too!
name = "Alice"
print(name == "Alice")   # True
print(name == "alice")   # False  ← case-sensitive!
```

---

# 🔀 if / elif / else

```
              ┌─────────────┐
              │  condition? │
              └──────┬──────┘
                     │
          True ◄─────┴─────► False
          │                   │
    ┌─────▼──────┐     ┌──────▼─────┐
    │ do this    │     │  do that   │
    └────────────┘     └────────────┘
```

```python
age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")
```

---

# 🔀 More if / elif / else Examples

```python
# Grade classifier
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
```

**Key rule:** Conditions are checked **top to bottom** — first `True` wins!

---

# 🧩 Logical Operators

Combine multiple conditions:

```python
# and — both must be True
age = 20
has_id = True
print(age >= 18 and has_id)   # True

# or — at least one must be True
is_weekend = False
is_holiday = True
print(is_weekend or is_holiday)   # True

# not — reverses True/False
is_raining = False
print(not is_raining)   # True
```

### Truth Table for `and`:
| A | B | A and B |
|---|---|---------|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

---

# 🔄 Truth Table for `or` and `not`

### `or`:
| A | B | A or B |
|---|---|--------|
| True | True | **True** |
| True | False | **True** |
| False | True | **True** |
| False | False | False |

### `not`:
| A | not A |
|---|-------|
| True | **False** |
| False | **True** |

```python
# Combining operators
x = 15
print(x > 10 and x < 20)    # True — between 10 and 20
print(not (x == 15))         # False
```

---

# 🔁 while Loops

A `while` loop repeats as long as a condition is `True`.

```python
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1   # Don't forget this! (infinite loop otherwise)

# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5
```

```
┌─────────────────┐
│  count <= 5?    │ ◄────┐
└────────┬────────┘      │
         │ True          │
    ┌────▼────┐          │
    │ print   ├──────────┘
    │ count+= │
    └─────────┘
         │ False
         ▼
       (done)
```

---

# ⛔ break and continue

```python
# break — exit the loop immediately
count = 0
while True:          # "infinite" loop
    count += 1
    if count == 5:
        break        # Stop when count reaches 5
print(f"Stopped at {count}")

# continue — skip to next iteration
for i in range(10):
    if i % 2 == 0:
        continue     # Skip even numbers
    print(i)         # Prints: 1, 3, 5, 7, 9
```

---

# 🔂 for Loops

A `for` loop iterates over a sequence.

```python
# range(stop) — 0 to stop-1
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(1, 6):
    print(i)   # 1, 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 11, 2):
    print(i)   # 0, 2, 4, 6, 8, 10

# Iterate over a string
for letter in "Python":
    print(letter)   # P, y, t, h, o, n
```

---

# 🎯 FizzBuzz — Classic Coding Challenge

Print numbers 1 to 30. But:
- If divisible by **3** → print "Fizz"
- If divisible by **5** → print "Buzz"
- If divisible by **both** → print "FizzBuzz"

```python
for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
```

Output: `1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz ...`

---

# 🎮 Live Demo: Number Guessing Game

```python
import random

secret = random.randint(1, 10)
attempts = 0

print("I'm thinking of a number between 1 and 10...")

while True:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You got it in {attempts} attempts!")
        break
```

---

# 🎯 Practice Exercises

**Exercise 1:** Write a program that prints all even numbers from 2 to 20.

**Exercise 2:** Ask the user for a password. Keep asking until they type "python123". Then print "Access granted!".

**Exercise 3:** Print a multiplication table for a number the user enters.
```
Enter number: 5
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

**Exercise 4:** Count how many vowels are in a word entered by the user.

---

# 📝 Assignment 2: Number Guessing Game

**Due:** Before Session 3

Write a program that:

1. Generates a **random number** between 1 and 100 (`import random`)
2. Asks the user to guess the number repeatedly
3. Gives hints: **"Too high!"** or **"Too low!"**
4. Counts the **number of attempts** and prints it when correct

**⭐ Bonus:**
- Add a maximum of 10 attempts; if exceeded, reveal the answer
- Add difficulty levels: Easy (1-50), Medium (1-100), Hard (1-500)

📁 Start with: `starter-code/assignment2_starter.py`
📄 Full details: `assignments/assignment2_guessing_game.md`

---

# 🎉 Session 2 Recap

Today you learned:

✅ Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
✅ `if`, `elif`, `else` — conditional branching
✅ Logical operators: `and`, `or`, `not`
✅ `while` loops — repeat while condition is True
✅ `for` loops — iterate over sequences
✅ `range()` — generate number sequences
✅ `break` — exit a loop early
✅ `continue` — skip to next iteration

**See you in Session 3! 🚀**
