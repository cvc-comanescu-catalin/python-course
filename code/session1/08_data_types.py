"""
Python knows what “type” everything is 
and it will not allow you to mix incompatible types without explicit conversion.
The main data types in Python are:
- Integer (int) — whole numbers, e.g., 42, -7, 0
- Float (float) — decimal numbers, e.g., 3.14, -0.001, 2.0
- String (str) — text, e.g., "Hello", 'Python', "123"
- Boolean (bool) — True or False


    
"""

# Integer — whole numbers
score = 100
year  = 2024
 
# Float — decimal numbers
price = 9.99
pi    = 3.14159
 
# String — text (use quotes)
greeting = "Hello!"
city     = 'Bucharest'
 
# Boolean — True or False
is_raining  = False
passed_exam = True
 
# You can check the type of a value using the built-in type() function:
print(type(score))       # <class 'int'>
print(type(price))       # <class 'float'>
print(type(greeting))    # <class 'str'>
print(type(is_raining))  # <class 'bool'>


# Type matters
# Python knows what type everything is, and it will not allow you to mix incompatible types without explicit conversion.
# For example, you cannot add a number and a string directly:
# This will cause an error:
# result = score + greeting  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# To combine different types, you need to convert them to a common type:
result = str(score) + " " + greeting  # Convert score to string and concatenate
print(result)  # "100 Hello!"



# String → number
age   = int("25")         # 25
age   = int("0x35", 16)   # 53 (hexadecimal to decimal)
# age   = int("test")     # This would cause a ValueError
price = float("9.99")     # 9.99
 
# Number → string
text = str(42)             # "42"
text = str(3.14)           # "3.14"
 
# Boolean conversions
bool(0)    # False
bool(1)    # True
bool("")   # False
bool("hi") # True
int(True)   # 1
int(False)  # 0

# One-liner (common pattern):
int(bool("hi")) # True → 1


"""
Dynamic typing is one of Python's core features that sets it apart from statically typed languages.
In Python, variables are not bound to a specific type at declaration.
Instead, the type is determined at runtime based on the assigned value.
This means that a single variable can hold data of different types throughout its lifetime
hence making Python a flexible and easy-to-use language for rapid development and prototyping.
"""

# Initially assigning an integer value
x = 42
print("x =", x, "| Type:", type(x))

# Reassigning a string value to the same variable
x = "Dynamic Typing in Python"
print("x =", x, "| Type:", type(x))