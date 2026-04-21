a = 10
b = 3
 
print(a + b)   # 13     Addition
print(a - b)   # 7      Subtraction
print(a * b)   # 30     Multiplication
print(a / b)   # 3.333  Division (always float)
print(a // b)  # 3      Floor Division
print(a % b)   # 1      Modulo (remainder)
print(a ** b)  # 1000   Exponentiation (10³)


x = 1 + 2 * 3 - 8 / 2 ** 3
x = 1 + (2 * 3) - (8 / (2 ** 3))
print(x)


x = 10     # Assign
x += 5     # x = x + 5   → 15
x -= 3     # x = x - 3   → 12
x *= 2     # x = x * 2   → 24
x /= 4     # x = x / 4   → 6.0
x //= 2    # x = x // 2  → 3.0
x **= 3    # x = x ** 3  → 27.0



first    = "Hello"
last     = "World"
full     = first + " " + last   # "Hello World"  — concatenation
repeated = "Ha" * 3             # "HaHaHa"       — repetition

text = "=" * 50
text += "\n ⭐⭐⭐ Welcome to Python ⭐⭐⭐ \n"
text += "=" * 50
print(text)