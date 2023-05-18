try:
    list = ["anil","Raju","Bheem"]
    i = int(input("Enter the value:"))
    print(list[i])
except:
    print("Its an error because you entered something greater than 2 or something else")
finally:
    print("This will get executed whether the exception is raised or not....")

# This is mainly used in writing code under the function and accessing later