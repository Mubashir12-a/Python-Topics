# Escape Sequences:

# print("Hello
#       World")    // Gives Syntax error because of new line.


# We use \n to avoid this error and write string in multi-lines:

print("Hello \nWorld");

#---------------------------------------------------------------------------

# print("Hello World "How are you"")   # Gives syntax error because we can use nested same type of quotes in string output.

# Here we use \" or \' for same types of quotes:

print("Hello World \"How are you\"")
# or 
print("Hello World 'How are you'")

#-----------------------------------------------------------------------------

# Print statement syntax:

# sep used to seprate objects like Hello ~ 1 ~ 2;
# end used to end thec ine without nextline print: means next statement starts after end not in next line.

print("Hello", 1, 2, sep="~", end="---");
print("World");

