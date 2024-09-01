import random

Inpt = input("Enter string: ") 

add = Inpt[0]
word = Inpt[1:]
word = word + add

def coding(n):
    
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    first = ''.join(random.sample(alphabets, 3))
    last = ''.join(random.sample(alphabets, 3))
    
    result = first + n + last
    return result



def decoding(m):
    
    decoded = m[3:-3]
    temp = decoded[len(decoded) - 1]
    decoded = temp + decoded
    decoded = decoded[:-1]
    
    return decoded





print("Coded word:",coding(word))  
 
DeC = coding(word)

print("Decoded word:",decoding(DeC)) 
    