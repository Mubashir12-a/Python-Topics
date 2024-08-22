# Strings is like array of chracters;

name = "Mubashir"
secound_name = "Ahmad"

print(name,secound_name) 

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
#print(name[8])   # Error because their are only 8 elements from 0-7;

# Slicing in string:

name = "mubashir ahmad"

print(name[0:8])   # Prints 0-7 it will not include last given index like 8;

print(name[0:-5])  # Prints full string but without last given index like -5 means dont include last 5 elements;

print(name[0::2])  # 0 is start :-: means full string, print after skiping 1; 

print(name[0:len(name) - 5])

print(name[-4:-2]) # From 4 to 2 but opposite side of string;

#----------------------------------------------

# More methods like:

"""

01. upper()
02. lower()
03. rstrip()
04. replace()
05. split()
06. capitalize()
07. center()
08. count()
09. endswith()
10. startswith()
11. find()
12. index()
13. isalnum()
14. isalpha()
15. islower()
16. isupper()
17. isprintable()
18. isspace()
19. istitle()
20. swapcase()
21. title()

"""

# upper(): Coverts to upper case.
name = "Hello World!"
print("01 :",name.upper())
print("\n")


# lower(): Converts to lower case.
name = "Hello World!"
print("02 :",name.lower())
print("\n")


# rstrip(): removes special characters.
name = "Hello World!"
print("03 :",name.rstrip("!"))
print("\n")


# replace(): replace any world or alphabet.
name = "Hello World!"
print("04 :",name.replace("World", "Earth"))
print("04 :",name.replace("l", "Y"))
print("\n")


# split(): splits strings into list.
name = "Hello World!"
print("05 :",name.split(' '))
print("\n")


# capitalize(): capitilize first alphabet and rest to lower case.
para = "hello WORLD, how are you!"
print("06 :", para.capitalize())
print("\n")


# center(): Adds spaces before strings like 50 - len(str) = space.
name = "Hello World!"
print("07 :", name.center(50))
print("\n")


# count(): counts any word or alphabet.
name = "Hello World!"
print("08 :", name.count("l"));
print("\n")


# endswith(): does string ends with given element.
name = "Hello World!"
print("09 :", name.endswith("!")) # True
print("09 :", name.endswith("?")) # false

# Does string ends with ' lo ' from index 2 to 5:
name = "Hello World!"
print("11 :", name.endswith("lo", 2, 5)) # True
print("\n")


# startswith(): does string starts with given element.
name = ">Hello World!"
print("10 :", name.startswith(">")) # True
print("10 :", name.startswith("?")) # false
print("\n")

# find(): returns the index of finding element.
sentence = "it's a computer language, it's a famous lang"
print("12 :", sentence.find("a"))
print("12 :", sentence.find("is")) # returns -1 as error.
print("\n")


# index(): same as find but returns error not -1:
sentence = "it's a computer language, it's a famous lang"
print("13 :", sentence.index("a"))
# print("11 :", sentence.index("is")) # returns error.
print("\n")


# isalnum(): checks string only contains a-z, A-Z, 0-9 nor even spaces.
text = "HelloWorld002"
name = "Hello World!"
sentence = "it's a computer language, it's a famous lang"
print("14 :", text.isalnum()) # True
print("14 :", sentence.isalnum()) # false
print("14 :", name.isalnum()) # false
print("\n")


# isalpha(): checks strings only contains a-z, A-Z.
text = "HelloWorld002"
text_2 = "helloWorld"
name = "Hello World!"
sentence = "it's a computer language, it's a famous lang"
print("15 :", text.isalpha())  # false
print("15 :", text_2.isalpha())  # true
print("15 :", sentence.isalpha())  # false
print("15 :", name.isalpha())  # false
print("\n")


# islower(): checks all chracters are lower or not but only isalpha()-->true strings.
text = "HelloWorld002"
text_2 = "helloWorld"
text_3 = "lowercase"
name = "Hello World!"
print("16 :", text.islower())  # False
print("16 :", text_2.islower())  # False
print("16 :", name.islower())  # False
print("16 :", text_3.islower())  # True
print("\n")


# isupper(): checks all chracters are upper or not but only isalpha()-->true strings.
text = "HelloWorld002"
text_2 = "helloWorld"
text_3 = "lowercase"
name = "HELLO WORLD"
print("17 :", text.isupper())  # False
print("17 :", text_2.isupper())  # False
print("17 :", name.isupper())  # True
print("17 :", text_3.isupper())  # False
print("\n")


# isprintable(): checks if all characters are printable or not like \n, \t are not printable:
text_2 = "helloWorld"
text_3 = "lowercase"
text_4 = "hello \n World"
print("18 :", text_4.isprintable())  # False
print("18 :", text_3.isprintable())  # True
print("18 :", text_2.isprintable())  # True
print("\n")


# isspace(): checks string are only made of spaces or not if yes then its true else false.
text_5 = "          "
text_3 = "lowercase"
text_4 = "hello \n World"
print("19 :", text_5.isspace())  # True
print("19 :", text_3.isspace())  # False
print("19 :", text_4.isspace())  # False
print("\n")


# istitle(): checks is given string first chracter is capitalize if yes then it true else false.
text = "HelloWorld002"
text_2 = "helloWorld"
text_3 = "lowercase"
text_4 = "Hello \n World"
print("20 :", text.istitle())  # False
print("20 :", text_2.istitle())  # False
print("20 :", name.istitle())  # True
print("20 :", text_3.istitle())  # False
print("\n")


# swapcase(): Converts lower case into upper into lower.
text = "HELLOWORLD002"
text_2 = "HelloWorld"
print("21 :", text.swapcase())  
print("21 :", text_2.swapcase())  
print("\n")


# title: coverts all first chracter of an word into capital.
sentence = "it is a computer language, it is a famous lang"
print("22 :", sentence.title()) 

print("\n")

