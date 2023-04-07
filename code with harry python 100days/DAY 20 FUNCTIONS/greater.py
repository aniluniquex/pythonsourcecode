def greaternum(a,b):
    if(a>b):
        print(a,"is greater")
    else:
        print(b,"is greater")

x = int(input("Enter a number:"))
y = int(input("Enter a number:"))
greaternum(x,y) # here we are calling a function

# if i wanna pass program in a function without writing any thing i would use pass
def lesser():
    pass #This will not throw any error