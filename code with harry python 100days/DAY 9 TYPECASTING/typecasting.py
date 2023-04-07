
''' conversion of one data type to another data type is called typecasting
    two types of conversion 
    1. explicit : as programmer we are doing this conversion
    2. implicit : conversion done by python itself

'''






# a = 1
a = "1"
b = "2"
# b = 2
# print(a+b) # This returns 12 if they are strings
print(int(a)+int(b)) # Here we did type casting which converts string to an integer

# Implicit type casting

c = 8
d = 5.5
print(c+d)

# here the above is implicit conversion which converted the value of c to float because of the data type converts into higher order from lower order to prevent memory loss
