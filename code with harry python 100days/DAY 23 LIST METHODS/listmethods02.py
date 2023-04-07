l = [10,23,56,55.1]
m = [22,78,334]
# m = l
# m[0] = 21


# m = l.copy()
# m[0] = 53


l.insert(4,100) #This will insery a element at a specific position
# here we inserted 100 at l at index 4

print(l)
# print(m)

m.extend(l)
print(m)

''' When we are using m.extend (l) we are adding list values of l to m
when we use the extend it affect the original datatype 
In the above case the value of m is 22,78,334 after extend the data type becomes
[22, 78, 334, 10, 23, 56, 55.1, 100]

'''

print(l+m) # This adds the l and m 
# [10, 23, 56, 55.1, 100, 22, 78, 334, 10, 23, 56, 55.1, 100]





# This will be changing the both the lists 
# but how we change a list without effecting the main list

'''when we use m = l.copy() then we copy the list l into m and when we are changing anything inside m then the l wont be effected 

so l.copy is used to change things
'''