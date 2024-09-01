'''
# Try-except:

In = input("Enter the Number: ")
print(f"Multiplecation table of {In} is: ")

"""
for i in range(1, 6):
    print(f"{int(In)} x {i} = {int(In)*i}")
"""
# If input was not number then program shows error and stops executing next program.    

try:
    for i in range(1, 6):
        print(f"{int(In)} x {i} = {int(In)*i}")
except Exception as e:
    # print(e)
    print("Type Error accured")
    
print("Next Program")

# handle specefic error:

try:
    num = int(input("Enter number: "))
except ValueError:
    print("Enter Valid Number")
    
    
try:
    num = int(input("Enter number: "))
    list = [5, 3, 8, 5]
    print(list[num])
except IndexError:
    print("Enter Valid Index Number")
    
'''   
    
    
#--------------------------------------------------------------------------------------
    

'''   
try:
    l = [1, 2, 3, 4, 5]
    i = int(input("Enter Index: "))
    print(l[i])
except:
    print("Error Accured")
finally:
    print("I am always Executed")


# We don't need finally in progrom because if we don't add finally program still get executed 
# Finally is used when we write it inside function:

def func(a,b):
    try:
        print(a*b)
        return 1
    except:
        print("Error Accured")
        return 0
       
    # print("I am without finally")  # This line will not be executed.
    
    finally:
        print("I am with finally")
        

func(5,10)

'''


#------------------------------------------------------------------


num = int(input("Enter Number greater then 10 & less then 20: "))

if (num < 10 or num > 20):
    raise ValueError("Check Number again")

# More error types on python documentation.