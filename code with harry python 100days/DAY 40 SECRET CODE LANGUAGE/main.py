choice = int(input("Enter 1 to encode and 2 to decode:"))

if (choice==1):
    name = input("Enter the string to encode:")
    if(len(name)>=3):
        print("hox"+name[1:len(name)]+name[0]+"kpp")
    elif(len(name)<3):
        print(name[::-1])
if(choice==2):
    name = input("Enter the string to decode:")
    if(len(name)>=3):
        print(name[len(name)-4]+name[3:len(name)-4])
    elif(len(name)<3):
        print(name[::-1])

# Yayy I done this!!!!!!!!!!!