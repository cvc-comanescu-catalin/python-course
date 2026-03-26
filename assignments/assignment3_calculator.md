# Assignment 3: Calculator with Functions 🧮

## 🎯 Objective

Build a fully functional command-line calculator using separate functions for each operation. This assignment practices defining functions, parameters, return values, menus, loops, and error handling.

---

## 📋 Requirements

### Part 1 — Arithmetic Functions
Create a separate function for each operation:

```python
def add(a, b):
    # Returns the sum of a and b

def subtract(a, b):
    # Returns the difference of a and b

def multiply(a, b):
    # Returns the product of a and b

def divide(a, b):
    # Returns the quotient of a and b
    # Handle division by zero!
```

Each function should:
- Accept **two parameters**
- **Return** the result (don't just print it!)
- The `divide()` function must handle division by zero gracefully

### Part 2 — Display Menu
Create a `display_menu()` function that prints:

```
==========================
      🧮 Calculator
==========================
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit
==========================
```

### Part 3 — Get User Numbers
Create a function `get_numbers()` that:
- Asks the user for two numbers
- Converts them to floats
- Returns both numbers

### Part 4 — Main Loop
In `main()`:
- Show the menu
- Get the user's choice
- Get two numbers (if not quitting)
- Call the appropriate function
- Display the result
- Loop until the user chooses "Quit"

---

## ⭐ Bonus / Stretch Goals

### Bonus 1 — Power and Square Root
Add two more operations using the `math` module:

```python
import math

def power(base, exponent):
    # Returns base raised to the exponent

def square_root(n):
    # Returns the square root of n
    # Handle negative numbers!
```

### Bonus 2 — Calculation History
Keep a list of all calculations performed in the session:
```
=== History ===
1. 10 + 5 = 15
2. 20 / 4 = 5.0
3. 3 ** 2 = 9
```

### Bonus 3 — Input Validation
What happens if the user types "abc" when asked for a number? Add `try/except` to handle `ValueError`.

---

## 💡 Hints

- Functions should **return** values, not print them:
  ```python
  def add(a, b):
      return a + b     # ✓ Correct
      # NOT: print(a + b)
  ```
- Division by zero check:
  ```python
  def divide(a, b):
      if b == 0:
          return "Error: Cannot divide by zero!"
      return a / b
  ```
- Get user input in a loop:
  ```python
  while True:
      choice = input("Enter choice: ")
      if choice == "5":
          break
      # handle other choices...
  ```
- `float()` handles both integers and decimals: `float("3.14")` → `3.14`, `float("5")` → `5.0`

---

## 📟 Example Session

```
==========================
      🧮 Calculator
==========================
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit
==========================
Choose an option (1-5): 1

Enter first number: 15
Enter second number: 7
Result: 15.0 + 7.0 = 22.0

==========================
Choose an option (1-5): 4

Enter first number: 10
Enter second number: 0
Error: Cannot divide by zero!

==========================
Choose an option (1-5): 5
Goodbye! 👋
```

---

## ✅ Checklist

Before submitting, make sure your calculator:

- [ ] Has a separate function for `add()`
- [ ] Has a separate function for `subtract()`
- [ ] Has a separate function for `multiply()`
- [ ] Has a separate function for `divide()` with division by zero handling
- [ ] Has a `display_menu()` function
- [ ] Shows a numbered menu to the user
- [ ] Accepts user input for the operation choice
- [ ] Asks for two numbers and performs the calculation
- [ ] Displays the result clearly
- [ ] Loops until the user chooses to quit

**Bonus:**
- [ ] `power()` and `square_root()` functions using `math`
- [ ] Calculation history displayed on request
- [ ] Handles invalid (non-numeric) input with try/except

---

## 📤 Submission Instructions

1. Open `starter-code/assignment3_starter.py`
2. Fill in all the `TODO` sections
3. Run and test all operations, including edge cases (divide by zero, invalid input)
4. Save your completed file as `assignment3_yourname.py`
5. Submit via the course platform or share the GitHub link

---

*💡 Tip: Functions should do ONE thing well. Separate the calculation logic from the display logic!*
