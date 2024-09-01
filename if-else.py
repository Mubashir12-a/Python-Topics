#Conditional statement:
'''
In python we don't use brackets for loops block.
In python identation is considered important thing
because it represents block of code.
'''

# age = int(input("Enter age: "))
age = 20

if(age >= 18):
    print("You can drive.")
else:
    print("You can't drive")
    
    
    
    
# temp = int(input("Enter temperature: "))
temp = 20

if(temp <= 0):
    print("Its cold temperature outside.")
elif(temp <= 25):
    print("Its normal temperature outside")
else:
    print("Its hot temperature outside.")    



#Nested if-else:

# GREATEST BETWEEN 3 NUMBERS:

x = 15
y = 7
z = 22

if(x > y):
    if(x > z):
        print(f"{x} is biggest num")
    else:
        print(f"{z} is biggest num")
else:
    if(y > z):
        print(f"{y} is biggest num")
    else:
        print(f"{z} is biggest num")



# short-hand if-else:

a = 10
b = 20

print("A") if a > b else print("=") if a == b else print("B")

# result = true if condition else false

