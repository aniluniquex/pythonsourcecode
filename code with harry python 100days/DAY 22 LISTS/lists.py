# lists are changable but tuple doesnot
# string can also contain diffrent data types


l = [10,20,56,"Anil",58.5555,"shubjam","lee","elon"]
print(l)
print(type(l)) # it is a list

# if we want to access the elements of l individually then we use
print(l[0]) # this prints 10
print()
# using for loop accessing individually
for i in range(0,5):
    print(l[i])

print("Yayy NOw we are demonstrating about negative indexing\n")
print(l[-3]) # This is negative indexing it will return 56 when 5 elements only

# by using in we can know whether an element is in the list or not

if 10 in l:
    print("Yes")
else:
    print("no")
if "il" in "Anil":
    print("yesss!!") # The samething also applies for string

print(l)
print(l[:])
print(l[1:8:2])