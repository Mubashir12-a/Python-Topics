import time

Let_Time = time.strftime('%H : %M : %S')

print(Let_Time)

hour = time.strftime('%H')
hour = int(hour)

if(hour < 6):
    print("Good Night")
elif(hour < 12):
    print("Good Morning")
elif(hour < 15):
    print("Good Afternoon")
elif(hour < 19):
    print("Good Evening")
else:
    print("Good Night")