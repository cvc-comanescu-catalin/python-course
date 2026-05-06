# List of dictionaries (common pattern!)
students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob",   "grade": 85},
    {"name": "Carol", "grade": 97},
]
 
# Access nested data
print(students[0]["name"])   # "Alice"
print(students[2]["grade"])  # 97
 
# Loop through list of dicts
for student in students:
    print(f"{student['name']}: {student['grade']}")
 
# Dictionary of lists
gradebook = {
    "Alice": [90, 85, 92],
    "Bob":   [78, 82, 80],
}
print(sum(gradebook["Alice"]) / len(gradebook["Alice"]))  # Average
