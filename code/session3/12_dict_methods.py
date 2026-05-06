person = {"name": "Bob", "age": 30, "city": "Paris"}
 
# Keys, values, items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Bob', 30, 'Paris'])
print(person.items())   # dict_items([('name', 'Bob'), ...])
 
# Looping
for key in person:
    print(key, "->", person[key])
 
for key, value in person.items():
    print(f"{key}: {value}")
 
# Check if key exists
if "name" in person:
    print("Name is:", person["name"])
