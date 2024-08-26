# User Defined functions:

def mean(x, y):
    return (x * y) / (x + y)

def Greastest(x,y):
    if(x > y):
        return x
    elif(x < y):
        return y
    else:
        return "Both are equal"
    
    
# pass use: its used to tell program that skip this because its incomplete so that program don't shoq error:
def add(x,y):
    pass

# num_1 = int(input("Enter Number-1: "))
# num_2 = int(input("Enter Number-2: "))

num_1 = 10
num_2 = 4

print("Mean is: ",mean(num_1, num_2))
print("Greatest is: ",Greastest(num_1, num_2))
print("Sum is: ",add(num_1, num_2))


# Functions arguments:

a = 10
b = 15

# Required arguments:

def average(x,y):
    print("Average is :", (x + y) / 2)
    
average(a,b)
average(20,25)

# Default arguments:

def multi(x, i = 1):
    print(f"{x} x {i} = {x * i}")
    
multi(5)   # It will take x = 5 & i as default value i.e; 1. because their are single arguments.
multi(5, 5)  # It will take x = 5 & i as new value i.e; 5 because their are 2 arguments.

def fullName(Fname, Lname, tag = "Student"):
    print(f"Name is {Fname} {Lname} Category: {tag}")
    
fullName("Mubashir", "Ahmad")
fullName("Mubashir", "Ahmad", "teacher")


# Functions with list, tuple, or set:

def TotalSum(*number):
    sum = 0
    for i in number:
        sum = sum + i
        
    return sum

print("Sum of numbers is:", TotalSum(2, 5, 8, 9, 4))