numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
# [start:stop]  — stop is NOT included
print(numbers[2:5])    # [2, 3, 4]
print(numbers[:4])     # [0, 1, 2, 3]  — from beginning
print(numbers[6:])     # [6, 7, 8, 9]  — to end
print(numbers[:])      # [0, 1, 2, ... 9]  — full copy
 
# [start:stop:step]
print(numbers[::2])    # [0, 2, 4, 6, 8]  — every 2nd
print(numbers[::-1])   # [9, 8, 7, ... 0]  — reversed!
 
# Visual:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#  ^
# [2:5] -> takes index 2, 3, 4 -> [2, 3, 4]