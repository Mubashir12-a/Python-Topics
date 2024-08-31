'''
if loop don't complete else block is printed 
but if we add break then else thinks loops is 
completed and else block skiped.
'''

for i in range(5):
    print(i)
    if i == 4:
        break
else:
    print("Sorry no more i value found")
    
    
for i in []:
    print(i)
else:
    print("Done")
    

for i in range(5):
    print(i)
else:
    print("Loop is not compeleted")
    
