# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics"]
}
 
# Accessing values
print(student["name"])      # "Alice"
print(student.get("age"))   # 20
print(student.get("gpa", 0.0))  # 0.0 (default if key missing)
 
# Adding / updating
student["email"] = "alice@example.com"  # Add new key
student["age"] = 21                     # Update existing key
 
# Deleting
del student["grade"]
removed = student.pop("age")
print(student.get("age"))   # None (age key removed)
print(removed)             # 21 (value of removed key)