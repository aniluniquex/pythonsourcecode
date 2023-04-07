for i in range(10):
    print(i)
# The above prints from 0 to n-1
print()
for k in range(10):
    print(k+1) # This will print from 1 to 10
# for i in range(1,20001):
#     print(i) # this will print from 1 to n-1
print("We are printing using step argument")
# now we using step argument
for i in range(1,10,2):
    print(i,end=",") # this prints 1,3,5,7,9

# here the above step argument value is 2 it skips the every n-1 elements after the first element and goes on