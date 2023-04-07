tup = (1,10,23,"Yellow",18)
print(type(tup),tup)

# But how would you print one elemnt in tuple
# t = (1)
# print(type(t),t) # This prints 1 and declares this as class int because when we are storing a single element in tuple then we have to write like this |||

t = (1,) # now this is a tuple consisiting single element
print(type(t),t)
# we cant change the elements in the tuple
# t[0] = 3
print(t[0]) # but we can access and print that element

#tuples also can be accessed as negative indexing
print(tup[-1]) # 18


# we can also check whether an element is in the tuple or not

if 23 in tup:
    print("Yayy 23 is in the tuple")

# we can also slice the elements in the tuple
print(tup[1:3]) # This will not change the tup but it creates the new tuple!!!
