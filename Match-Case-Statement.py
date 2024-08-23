User = int(input("Enter Rank (1, 2, 3, or above): "))

match User:
    
    case 1:
        print("You got Gold medal")
        
    case 2:
        print("You got Silver medal")
        
    case 3:
        print("You got Bronze medal")
        
    case _ if User >= 10:
        print("Try Next Time")
        
    case _ if User < 10 and User > 3:
        print("You Won cash Prize")
        
    case _ :
        print("Invalid Input By User")
        
        