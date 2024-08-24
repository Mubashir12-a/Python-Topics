# print numbers 0 - 10:

i = 0;   # initialization

while i <= 10:         # Condition check
    print(i, end=" ")
    i = i + 1          # Increament
    
print("\n")


# take user password and Grant access:

password = "mubashir"
user_pass = input("Enter Password: ")

while user_pass != password:
    user_pass = input("Try again: ")
else:
    print("Access Granted")
