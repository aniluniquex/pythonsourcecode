a = int(input("Enter the number:"))

if (a<0):
    print("The value of a is negative")
elif(a>0):
    if(a<=10):
        print("The value of a is b/w 1 and 10")
    elif(a>11 and a<=20):
        print("The value of a is b/w 11 and 20")
    else:
        print("The value of a is greater than 20") 
else:
    print("The value of a is zero")  
    