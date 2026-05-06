
# What does this print?
def mystery(x, y=10):
    return x * y
 
print(mystery(3))
print(mystery(3, 5))

# What's the scope issue here?
def double():
    result = x * 2   # Is this okay?
    print(result)
 
x = 5
double()

# import Random
# Random.randint(1, 10)  # What does this do?

# def get_value(prompt, value_min=0, value_max=100):
#     while True:
#         try:
#             value = int(input(prompt))
#             if value_min <= value <= value_max:
#                 return value
#             else:
#                 print(f"Please enter a number between {value_min} and {value_max}.")
#         except ValueError:
#             print("That's not a valid number. Please try again.")

# age = get_value("Enter your age: ", 0, 120)
# print(f"You entered: {age}")

# import util
# age = util.get_value("Enter your age: ", 0, 120)
# print(f"You entered: {age}")

from util import get_value, read_float_ranged, read_float
age = get_value("Enter your age: ", 0, 120)
print(f"You entered: {age}")

temperature = read_float_ranged("Enter the temperature in Celsius: ", -50.0, 50.0)
print(f"You entered: {temperature} °C")

import pydoc
#help(pydoc)
pydoc.help(get_value)
pydoc.help(read_float)