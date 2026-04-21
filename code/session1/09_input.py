"""
input()  pauses the program and waits for the user to type something.
The user can enter any text, and when they press Enter, the input() function will return that text as a string.
You can also provide a prompt message to input() to guide the user on what to enter.
"""

name = input("What is your name? ")
print("Hello,", name)
age = input("How old are you? ")
print("You are", age, "years old.")

# ⚠  Important:  input()  always returns a string!
# If you want to treat the input as a number, you need to convert it using int() or float():
print(type(age))  # <class 'str'>  — age is a string
print("You are " + age + " years old.") # This works because age is a string, but it will not work if we want to do math with it.
new_age = age + 1  # This will cause an error because you cannot add a string and an integer.
# To fix this, we need to convert age to an integer first: 
new_age = int(age) + 1  # Convert age to an integer before adding 1
print("Next year, you will be " + str(new_age) + " years old.")
