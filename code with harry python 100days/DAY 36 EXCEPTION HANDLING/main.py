a = input("Enter a number:")
print(f"The multiplication of a {a} table is:")
try:
    for i in range(0,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    print("You have given Invalid input")
# The above raises an exception


print("some lines of code")
print("End of program")
    