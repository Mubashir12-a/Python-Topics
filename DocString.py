# Doc-String

# Always written first inside function else its considered as comment. 

def sqr(n):
    '''This function calculates the square root of 
    any real number and prints it on display'''
    
    return n**2

print(sqr(5))
print(sqr.__doc__)

