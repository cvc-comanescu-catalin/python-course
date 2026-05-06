fruits = ["apple", "banana"]
 
# Adding items
fruits.append("cherry")        # Add to end -> [..., "cherry"]
fruits.insert(1, "blueberry")  # Insert at index 1
 
# Removing items
fruits.remove("banana")        # Remove by value
last = fruits.pop()            # Remove & return last item
item = fruits.pop(0)           # Remove & return at index 0
 
# Other useful methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()                 # Sort in place -> [1, 1, 2, 3, 4, 5, 6, 9]
numbers.reverse()              # Reverse in place
print(len(numbers))            # 8
print(numbers.count(1))        # 2 — how many times 1 appears
print(numbers.index(5))        # 4 — index of value 5
