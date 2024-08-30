dem = {
    "Name": "Mubashir",
    "Course": "BCA",
    "Age": 20
}

print(type(dem))

print(dem)
print(dem["Name"])
print(dem.get('Name'))
print("\n",dem.keys())
print("\n",dem.values())

print(f"\n{dem["Name"]} is doing {dem["Course"]} at age of {dem.get('Age')}")

# Dictionary is ordered and mutable.



# for loop with dictionary:
print("\n\tUsing For loop:")

for i in dem.keys():
    print(dem[i])
    print(f"The value corresponding to the key {i} is {dem[i]}")
    

print("\n")
print(dem.items())
print("\n")


for i, j in dem.items():
    print(f"The value corresponding to the key {i} is {j}")
    



# Dictionary Methods:
print("\nDictionary-Methods:\n")

# Update:
print("Update():")

emp_1 = {
    "Em-001": 9,
    "Em-002": 3,
    "Em-003": 6,
    "Em-004": 5
}

emp_2 = {
    "Em-005": 9,
    "Em-006": 10,
    "Em-007": 2,
    "Em-008": 8
}

emp_1.update(emp_2)

print(emp_1)

print("\n")

# Clear:
print("clear():")

emp_3 = {"h1" : 258, "h2" : 147, "h3" : 369}
print(emp_3)
emp_3.clear()
print(emp_3)

print("\n")

# Pop:
print("pop():")

emp_3 = {"h1" : 258, "h2" : 147, "h3" : 369}
print(emp_3)
emp_3.pop("h2")
print(emp_3)

print("\n")


# Popitem: removes last item.
print("popitem():")

emp_3.popitem()
print(emp_3)


# del emp_3
# del emp["h1"]

