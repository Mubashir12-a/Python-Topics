for i in range(1, 11):
    print(f"5 x {i} = {5*i}")
    if i==5:
        break
    
print("For-Loop Ended because of Break")

i = 1;
while i <= 10:
    print(f"5 x {i} = {5*i}")
    if i==5:
        break
    i = i + 1
    
print("While-Loop Ended because of Break")


for i in range(1, 11):
    if i==5:
        print("Skip")
        continue
    print(f"5 x {i} = {5*i}")
    
print("For-Loop skiped 5th iteration because of continue")

j = 1;
while j <= 10:
    if j==5:
        print("Skip")
        j = j + 1
        continue
    print(f"5 x {j} = {5*j}")
    j = j + 1
    
print("While-Loop skiped 5th iteration because of continue")
