
list = [1, 5, 8]
print(type(list))



print("\nList elements are accessed by their index number:\n")
# List elements are accessed by their index number:

print(list[0])  # 1
print(list[1])  # 5
print(list[2])  # 8
# Negative Indexing:
print(list[len(list) - 2]) # 5
print(list[-1]) # 8
print(list[-3]) # 1




print("\nConditions with list:\n")
# Conditions with list:

n = 5

if n in list:
    print(f"Yes, {n} is inside list")
else:
    print(f"No, {n} is not inside list")



print("\nIndex trough loops with two lists:\n")
# Index trough loops with two lists:

names = ["Student-01", "Student-02", "Student-03", "Student-04",]
marks = [58, 92, 74, 65]

for i, j in zip(names, marks):
    print(f"{i} got {j} marks in exams")
    
# zip(): function in Python is used to combine two or more iterables 
# (like lists, tuples, etc.) into a single iterable of tuples.

Elmt = ["Hello", True, 10, 25.6, 'M']

if "Hello" in Elmt:
    print("Yes")
else:
    print("No")
    
    
if "Hell" in "Hello":
    print("Yes")
else:
    print("No")
    

if True in Elmt:
    print("Yes")
else:
    print("No")
    
    
if False in Elmt:
    print("Yes")
else:
    print("No")
    
    

print("\nList methods:\n")
# List methods:

nums = [1, 5, 9, 7, 5, 3]

print(nums[:])  # To print full list.
print(nums[:-1])  # To print full list except last element.
print(nums[1:-1])  # To print full list except last element & First Element of list.
print(nums[0::2])  # From 0 index to last index in jump of 2.
print(nums[::-1])  # From first index to last index in jump of -1 (means jump 1 in reverse order).



print("\nList comprehension:\n")
# List comprehension:
'''
 It allows you to generate a new list by applying an expression to each item in an existing iterable
(like a list or range) and optionally including a condition.
'''

lst = [i for i in range(1,6)]  # Create list from 1 to 5.
print(lst)

lst_2 = [i*2 for i in range(1,6)]  # Create list from 1 to 5 by multiplying with 2.
print(lst_2)

even_nums = [i for i in lst if i%2 == 0]  # Get elements from lst and print only those who mets the condition (true).
print(even_nums)




print("\nMORE lIST METHODS AND MANUPLATION:\n")
# MORE lIST METHODS AND MANUPLATION:

'''
01. append()
02. sort()
03. sort(reverse = True)
04. reverse()
05. index()
06. count()
07. copy()
08. insert()
09. extend()
'''

vxr = [7, 8, 3, 4, 3]
print(vxr,"\n")

print("1. append():")
# append:
vxr.append(5)
print(vxr,"\n")


print("2. sort():")
# sort: In ascending oirder:
vxr.sort()
print(vxr,"\n")


print("3. sort(reverse = True):")
# sort: In descending oirder:
vxr.sort(reverse = True)
print(vxr,"\n")


print("4. reverse():")
# reverse: reverse a list
vxr.reverse()    # list was reversed previous sort function so it reversed it back
print(vxr,"\n")


print("5. index():")
# index: returns index number on given argument:
print(vxr.index(5),"\n")


print("6. count():")
# count: to count how many times value repeats in list:
print(vxr.count(3),"\n")


print("7. copy():")
# copy: copies list elements to another list:
new_vxr = vxr.copy()
print(new_vxr,"\n")

'''
because we can't do like:

new_vxr = vxr

because it will be its refrence not another list if
we do any changes in new_vxr the original list also be modified 
because memory address is same just names are diffrent i.e; refrence
'''


print("8. insert():")
# insert: we can insert any value on any index number:
vxr.insert(0, 245)
print(vxr,"\n")

vxr.insert(len(vxr), 125)
print(vxr,"\n")


print("9. extend():")
# extend: used to extend an list with another list elements or by new elements::
new_vxr_2 = [100, 200, 300]
vxr.extend(new_vxr_2)
print(vxr,"\n")

vxr.extend((10, 20, 30))
print(vxr,"\n")
