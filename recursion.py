# Recursion is same as functions but in recursion function call itself inside function works like loop:

# Print 1 to 10 using recursion:

def Pn(n):
    if n > 10:
        return 0
    
    print(n)
    return Pn(n + 1)

Pn(1)

'''
The function Pn(n) recursively prints numbers from n up to 10. 
When n exceeds 10, it stops and returns 0. The initial call Pn(1) 
starts printing from 1 and continues until 10.
'''

# Factorial of any number:

def fact(n):
    if(n == 0 or n == 1):
        return 1
    
    return n * fact(n - 1)

print(fact(5))

# Dry-Run:
'''
Initial Call: fact(5)

Since n is not 0 or 1, it returns 5 * fact(4).
Next Call: fact(4)

Since n is not 0 or 1, it returns 4 * fact(3).
Next Call: fact(3)

Since n is not 0 or 1, it returns 3 * fact(2).
Next Call: fact(2)

Since n is not 0 or 1, it returns 2 * fact(1).
Next Call: fact(1)

Since n is 1, it returns 1.
Returning Values:

fact(2) returns 2 * 1 = 2.
fact(3) returns 3 * 2 = 6.
fact(4) returns 4 * 6 = 24.
fact(5) returns 5 * 24 = 120.
Final Output: The print(fact(5)) statement outputs 120.
'''

# Fibonacci series:

def Srs(r, a = 0, b = 1):
    sum = a + b
    
    if( sum > r):
        return 0
    
    print(sum)
    
    a = b
    b = sum
    
    return Srs(r, a, b)

Srs(25)
    