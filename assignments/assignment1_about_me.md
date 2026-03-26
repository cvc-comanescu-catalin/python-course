# Assignment 1: "About Me" Script 👤

## 🎯 Objective

Write a Python script that collects personal information from the user and displays a nicely formatted summary. This assignment practices variables, data types, user input, type conversion, and string formatting.

---

## 📋 Requirements

### Part 1 — Collect User Information
Ask the user for the following using `input()`:
1. Their **name**
2. Their **age** (convert to integer)
3. Their **favorite hobby**

### Part 2 — Calculate Birth Year
Using the current year (you can hardcode `2024` or use a variable), calculate the **approximate year they were born**.

```
birth_year = current_year - age
```

### Part 3 — Display Summary
Print a formatted summary like:

```
=====================================
           About Me
=====================================
Hi, I'm Alice!
I'm 25 years old, born around 2001.
My favorite hobby is hiking.
=====================================
```

---

## ⭐ Bonus / Stretch Goals

### Bonus 1 — Two-Number Arithmetic
Ask the user for two numbers and display:
- Their **sum**
- Their **difference**
- Their **product**
- Their **quotient** (handle division by zero!)

### Bonus 2 — Personalization
Add more fields: favorite food, favorite color, hometown. Include them in the summary.

### Bonus 3 — f-string Formatting
Use f-strings to format the output (no `+` string concatenation).

---

## 💡 Hints

- `input()` always returns a **string** — use `int()` to convert age
- You can use `print()` multiple times or one `print()` with `\n` for newlines
- A dashed separator: `print("=" * 37)` prints 37 equal signs
- f-string example: `f"Hi, I'm {name}!"` — the variable name goes inside `{}`
- Current year hint: you can also use `import datetime; datetime.datetime.now().year`

---

## 📟 Example Session

```
What is your name? Alice
How old are you? 25
What is your favorite hobby? hiking

=====================================
           About Me
=====================================
Hi, I'm Alice!
I'm 25 years old, born around 1999.
My favorite hobby is hiking.
=====================================
```

With bonus:
```
Enter the first number: 10
Enter the second number: 3
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.33
```

---

## ✅ Checklist

Before submitting, make sure your script:

- [ ] Asks the user for their name
- [ ] Asks the user for their age and converts it to an integer
- [ ] Asks the user for their favorite hobby
- [ ] Calculates the birth year correctly
- [ ] Displays a formatted summary with all the information
- [ ] Uses f-strings or string concatenation for formatting
- [ ] Runs without errors

**Bonus:**
- [ ] Asks for two numbers and displays arithmetic results
- [ ] Handles division by zero gracefully

---

## 📤 Submission Instructions

1. Open `starter-code/assignment1_starter.py`
2. Fill in all the `TODO` sections
3. Test your script by running it
4. Save your completed file as `assignment1_yourname.py`
5. Submit via the course platform or share the GitHub link

---

*💡 Tip: If you get stuck, re-read the Session 1 slides or ask in the course chat!*
