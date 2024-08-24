# Print numbers from 1 - 10:

for i in range(10):
    print(i, end=" ")
    
print("\n")

# The loop will print from 0 - 9 because i not initialized and range means print less then 10 not equal to 10:

# for 1 - 10 we do:

for i in range(1, 11):
    print(i, end=" ")
    
print("\n")

# Step in for loop: 

for i in range(0, 11, 2):
    print(i, end=" ")
    
print("\n")

# For loop with strings and list:

name = "Mubashir"

for i in name:
    print(i, end=" ")
    
print("\n")


for i in range(0, len(name), 2):
    print(name[i], end=" ")
    
print("\n")


fruits = ["Apple", "Orange", "Kiwi", "Tomato", "Potato", "Watermelon"]

for i in fruits:
    print(i, end=",")

print("\n")

for i in fruits:
    if(i == "Potato"):
        print(i, "is not a fruit")
        for j in i:
            print(j, end=" ")
            
print("\n")
 
  
