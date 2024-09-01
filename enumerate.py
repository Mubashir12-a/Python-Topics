marks = [12, 56, 35, 78, 95, 45, 68]

index = 0

for i in marks:
    print(i)
    if(index == 3):
        print("End")
        break
    index += 1
    
    
for index, i in enumerate(marks):
    print(i)
    if(index == 3):
        print("End")
        break
    
    
    
for index, i in enumerate(marks, start = 2):
    print(i)
    if(index == 3):
        print("End")
        break
    
    
'''
In the given code, the enumerate() function is used to iterate over the marks list,
starting with an index of 2. As the loop progresses, it prints each element of the 
list along with its index.

During the first iteration, the index is 2, and the value 90 is printed. 
In the second iteration, the index becomes 3, and the value 80 is printed. 
At this point, the code checks if the index is 3, which is true, 
so it prints "End" and then exits the loop due to the break statement. 
As a result, only the values 90 and 80, along with "End", are printed before the loop terminates.
'''