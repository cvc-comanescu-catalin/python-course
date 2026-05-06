# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [42, "hello", True, 3.14]
empty = []
print(type(fruits))  # <class 'list'>
 
# Indexing — starts at 0!
#   Index:  0        1         2
fruits = ["apple", "banana", "cherry"]
 
print(fruits[0])    # "apple"
print(fruits[1])    # "banana"
print(fruits[-1])   # "cherry"  <- negative index from end
print(fruits[-2])   # "banana"
print(fruits[-3])   # "apple"