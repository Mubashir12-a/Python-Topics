# variable is a container which contains data in memory:

a = 10;      # " a " is variable name and ' 10 ' is data stored in it.
print(a);

a = 20;
print(a);    # overwrites Data stored in variable.

a = a + a;
print(a);    # output is 40;

b = "Mubashir";   # string;
print(b);

b_2 = " Ahmad ";
print(b + b_2);     # concat;

# print(b + a);    # Error because only strings concat not int, float, bool etc;

#---------------------------------------------------

# Data types:

x = 10;
y = 10.5;
z = "name";
q = True;

print(type(x));
print(type(y));
print(type(z));
print(type(q));