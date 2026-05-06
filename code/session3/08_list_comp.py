# Traditional way:
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
 
# List comprehension — same result in one line!
squares = [n ** 2 for n in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]
 
# With a condition (filter):
evens = [n for n in range(20) if n % 2 == 0]
print(evens)     # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
 
# Transform strings:
words = ["hello", "world", "python"]
upper = [word.upper() for word in words]
print(upper)     # ['HELLO', 'WORLD', 'PYTHON']

# With a condition (filter) and transformation:
short_words = [word.upper() for word in words if len(word) <= 5]
print(short_words)  # ['HELLO', 'WORLD'] 