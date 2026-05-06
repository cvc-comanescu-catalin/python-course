fruits = ["apple", "banana", "cherry", "date"]
 
# Simple loop
for fruit in fruits:
    print(fruit)
 
# Loop with index using enumerate()
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry
# 3: date
 
# Loop and modify (use range + len)
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)   # [2, 4, 6, 8, 10]
