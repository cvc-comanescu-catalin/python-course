"""
Comparison operators are used to compare values and return a boolean result (True or False).
They are fundamental in controlling the flow of a program, especially in conditional statements (if, elif, else) and loops (while, for).
Understanding how to use comparison operators is essential for making decisions in your code and for implementing logic that depends on the relationships between values.
For example, you can use comparison operators to check if a user is old enough to access certain content, to compare scores in a game, or to validate input data.
In Python, you can also chain comparison operators for more complex comparisons. For example:
x = 10
print(5 < x < 15)  # True  — x is greater than 5 and less than 15
This allows you to check multiple conditions in a single expression, making your code more concise and readable.
"""

x = 10
y = 5
 
print(x == y)   # False  — Equal to
print(x != y)   # True   — Not equal to
print(x > y)    # True   — Greater than
print(x < y)    # False  — Less than
print(x >= 10)  # True   — Greater than or equal
print(x <= 9)   # False  — Less than or equal

# Comparison operators look at variables but do not change the variables
print(x)  # 10
print(y)  # 5

is_x_greater = x > y
print(is_x_greater)  # True
print(5 < x < 15)  # True  — x is greater than 5 and less than 15

"""
Remember:  “=” is used for assignment.
“==” is used for comparison (equality check).
This is a common source of bugs for beginners, so always double-check that you are using the correct operator for your intended purpose.
"""

# Works with strings too!
name = "Alice"
print(name == "Alice")   # True
print(name == "alice")   # False  ← case-sensitive!
print(name != "Bob")     # True
print(name > "Bob")      # False  — "Alice" comes before "Bob"