x = int(input("Enter the value of x:"))

match(x):
    case 1:
        print("It is one")
    case 2:
        print("It is two")
    case 3:
        print("It is three")
    case 4:
        print("It is four")
    
    
    case _ if (x!=90):
        print(x,"is not 90")
    case _ if (x!=80):
        print(x,"is not 80")    
    case _:
        print("It is something else")


# here in python there is no need to use break statment because if a cas e is matched then it executes only that part and dont execute the remaining part
