# Tuple is same as list but it's immutable and uses () braces:


tuple_1 = (1, 2, 8, 4)
print(type(tuple_1))
print(tuple_1)

# Tuple is immutable we can't add or modify tuple values:

# tuple[4] = 45
# print(tuple)  # Error we can't assign new element;

print([tuple_1[0]])
print([tuple_1[3]])


for i in tuple_1:
    print(i)
    

if 8 in tuple_1:
    print("Yes")
else:
    print("No")


# Slicing in tuple:

tuple_2 = tuple[0:2] # We create another tuple because we can't change tuple.
print(tuple_2)

'''
Tuple can't be modified or changed directly so we do indirectly 
where original tuple is not changing or modifying but a another 
new tuple we carry changed or modified things
'''


# Tuple Methods:


nums = (20, 50, 78, 98, 67)
print(nums)         # Tuple

temp = list(nums)    # convert tuple into list with help of list() build in function;
temp.append(11)    # Add element into list
print(temp)      # We can use all list methods after convertion

nums = tuple(temp)    # Convert list back to tuple with help of tuple() inbuild function;
print(nums)


# Concate 2 tuples without convertion:

t_1 = (1, 2, 3, 4, 5)
t_2 = (6, 7, 8, 9, 10)
t_3 = t_1 + t_2
print(t_3)


# Count(), index():

tup = (1, 3, 4, 7, 4, 3, 4)
temp_2 = tup.count(4)
print(temp_2)

temp_2 = tup.index(4)
print(temp_2)

temp_2 = tup.index(4, 3, len(tup))   # index(find, start, end)
print(temp_2)





