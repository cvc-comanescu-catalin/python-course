# Assignment 4: Student Gradebook 📚

## 🎯 Objective

Build a menu-driven student gradebook application using dictionaries. This assignment practices dictionaries, loops, functions, user input validation, and data manipulation.

---

## 📋 Requirements

### Part 1 — Data Storage
Use a **dictionary** to store student data:
```python
gradebook = {}  # key: student name, value: grade (or list of grades)
```

### Part 2 — Add a Student
Create a function `add_student(gradebook)` that:
- Asks for the student's **name**
- Asks for their **grade** (0–100)
- Validates the grade (must be a number between 0 and 100)
- Adds them to the gradebook
- Prints confirmation: `"Added Alice with grade 92."`

### Part 3 — View All Students
Create a function `view_all_students(gradebook)` that:
- If the gradebook is empty, prints: `"No students yet."`
- Otherwise, prints a formatted table:
  ```
  ==============================
        Student Gradebook
  ==============================
  Alice          →  92
  Bob            →  85
  Carol          →  97
  ==============================
  ```

### Part 4 — Search for a Student
Create a function `search_student(gradebook)` that:
- Asks for a student name
- If found: prints their name and grade
- If not found: prints `"Student not found."`

### Part 5 — Calculate Class Average
Create a function `calculate_average(gradebook)` that:
- If no students, prints `"No students to average."`
- Otherwise calculates and prints the average grade:
  ```
  Class average: 91.33
  ```

### Part 6 — Menu-Driven Loop
Create a `display_menu()` function and a main loop:

```
==================================
       📚 Student Gradebook
==================================
1. Add student
2. View all students
3. Search for a student
4. Calculate class average
5. Quit
==================================
```

---

## ⭐ Bonus / Stretch Goals

### Bonus 1 — Remove a Student
Add menu option 6 to delete a student from the gradebook.

### Bonus 2 — Highest & Lowest
After viewing all students, also show the highest and lowest scoring students.

### Bonus 3 — Grade Distribution
Add a function that shows how many students fall in each letter grade:
```
Grade Distribution:
A (90-100): 2 students
B (80-89):  1 student
C (70-79):  0 students
D (60-69):  0 students
F (0-59):   0 students
```

### Bonus 4 — Multiple Grades Per Student
Instead of a single grade, store a **list** of grades per student. Calculate their **individual average**:
```python
gradebook = {
    "Alice": [90, 85, 92],
    "Bob":   [78, 82, 80],
}
```

---

## 💡 Hints

- Check if a key exists in a dictionary: `if name in gradebook:`
- Get all values: `gradebook.values()` — returns all grades
- Calculate average:
  ```python
  avg = sum(gradebook.values()) / len(gradebook)
  ```
- Format a float to 2 decimal places: `f"{avg:.2f}"`
- For input validation:
  ```python
  try:
      grade = float(input("Grade: "))
      if 0 <= grade <= 100:
          # valid
      else:
          print("Grade must be between 0 and 100!")
  except ValueError:
      print("Please enter a number!")
  ```

---

## 📟 Example Session

```
==================================
       📚 Student Gradebook
==================================
1. Add student
2. View all students
3. Search for a student
4. Calculate class average
5. Quit
==================================
Choose option (1-5): 1

Enter student name: Alice
Enter grade (0-100): 92
✓ Added Alice with grade 92.

Choose option (1-5): 1
Enter student name: Bob
Enter grade (0-100): 85
✓ Added Bob with grade 85.

Choose option (1-5): 2

==============================
      Student Gradebook
==============================
Alice          →  92
Bob            →  85
==============================

Choose option (1-5): 4

Class average: 88.50

Choose option (1-5): 3
Enter name to search: Carol
Student 'Carol' not found.

Choose option (1-5): 5
Goodbye! 👋
```

---

## ✅ Checklist

Before submitting, make sure your gradebook:

- [ ] Uses a dictionary to store students and grades
- [ ] `add_student()` — adds a student with grade validation
- [ ] `view_all_students()` — displays all students formatted
- [ ] `search_student()` — looks up a student by name
- [ ] `calculate_average()` — computes the class average
- [ ] Has a working menu with a loop
- [ ] Handles the case where the gradebook is empty
- [ ] Validates that the grade is a number between 0 and 100

**Bonus:**
- [ ] Remove student option
- [ ] Shows highest and lowest student
- [ ] Grade distribution (A/B/C/D/F)
- [ ] Multiple grades per student with individual averages

---

## 📤 Submission Instructions

1. Open `starter-code/assignment4_starter.py`
2. Fill in all the `TODO` sections
3. Test all menu options, including edge cases (empty gradebook, missing student, invalid grade)
4. Save your completed file as `assignment4_yourname.py`
5. Submit via the course platform or share the GitHub link

---

*💡 Tip: Test with an empty gradebook first, then add a few students and test all options!*
