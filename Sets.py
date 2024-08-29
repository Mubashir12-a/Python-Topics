'''
a set is an unordered collection of unique elements. 
Sets are useful when you want to store items without duplicates
and perform operations like unions, intersections, and differences.
''' 

set_1 = {1, 2, 3, 2, 4}
print(set_1)  # Repeated Element will not display;

# print(set_1[1]) 

'''
sets are unordered collections, meaning they don't support indexing 
like lists or tuples. Therefore, you can't access elements in a set 
using an index (e.g., set_1[1]).
'''

set_2 = {}
print(type(set_2))   # show dictionary because dictianary is also uses curly braces


set_2 = set()
print(type(set_2))   # Now it will show its type as set

# For loop with set:

for i in set_1:
    print(i)
    
    
    
# Set Methods:

# Union:
# It will remove duplicates and combine both sets withoput dublicates:
print("\t\tUnion():")

s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 5, 9, 11}

print(s1.union(s2))



# update:
# Used to change set or make changes like add another set to it:
print("\t\tupdate():")

s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 5, 9, 11}

s1.update(s2)
print(s1)



# Intersection:
# It will print only dublicate values in sets:
print("\t\tIntersection():")

s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 5, 9, 11}

print(s1.intersection(s2))



# Intersection_update:
# Works same as update() but only for intersection.
print("\t\tIntersection_update():")

s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 5, 9, 11}

s2.intersection_update(s1)
print(s2)



# symetric_diffrence:
# it will remove all dulicated values and prints only those who don't have any dublicate
print("\t\tsymetric_difference():")

s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 5, 9, 11}

print(s1.symmetric_difference(s2))



# symetric_difference_update:
# Works same as update.
print("\t\tsymetric_difference_update():")

s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 5, 9, 11}

s1.symmetric_difference_update(s2)
print(s1)



# isdisjoint:
# if 2 sets values aren't same then its true else ite false.
print("\t\tisdisjoint():")

s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 5, 9, 11}

print(s1.isdisjoint(s2))  # False

s4 = {1, 2, 3, 4}
s5 = {5, 6, 7, 8}

print(s4.isdisjoint(s5))  # True



# issupperset:
# Checks is a sets value is already in another set if yes then True else false.
print("\t\tissupperset():")

s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 5, 9, 11}

print(s1.issuperset(s2))  # False

s4 = {1, 2, 3, 4}
s6 = {1, 2, 3, 4}  
s7 = {3, 4}        

print(s4.issuperset(s6))  # True
print(s4.issuperset(s7))  # True
print(s6.issuperset(s7))  # True



# issubset:
# Its opposite of issupperset.
print("\t\tissubset():")

s1 = {1, 2, 3, 4, 5}
s2 = {1, 3, 5, 9, 11}

print(s1.issubset(s2))  # False

s4 = {1, 2, 3, 4}
s6 = {1, 2, 3, 4}  
s7 = {3, 4}       

print(s4.issubset(s6))  # True

print(s4.issubset(s7))  # False
print(s7.issubset(s4))  # True

print(s6.issubset(s7))  # False
print(s7.issubset(s6))  # True



# add:
# To add single element to set.
print("\t\tadd():")

s4 = {1, 2, 3, 4, 5}
print(s4)

s4.add("Hello")
print(s4)



# remove / discard:
# To remove any element from set, if element was not in set remove() raise error but discard will not raise error.
print("\t\tremove() / discard():")

s4 = {1, 2, 3, 4, 5, "Hello"}
print(s4)

s4.remove("Hello")
print(s4)

# s4.remove("World")   # Error because element is not in set.
# print(s4)

s4.discard("Hello")  # No error even element is not in set.
print(s4)



# pop:
# Will remove any element from set because set is unodered else in list it pops index 0 
# and prints which element was poped.
print("\t\tpop():")

s3 = {"Tokyo", "Landon", "Germany", "Japan", "Turkey"}
print(s3)

# s3.pop()
Pop_item = s3.pop()
print(Pop_item)
print(s3)



# del:
# used to delete set or list.
print("\t\tdel:")

s3 = {1, 2, 3, 4, 5}
print(s3)

del s3
# print(s3)  # Error because s3 is deleted



# clear:
# used to clear-->(remove all items) from set or list and makes it empty without deleting it.
print("\t\tclear():")

s3 = {1, 2, 3, 4, 5}
print(s3)

s3.clear()
print(s3)