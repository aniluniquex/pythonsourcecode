tup = (1,0,5,2,1,8,9,23)
# we cant change this tuple directly but we can change using list

l = list(tup)
# print(type(l))
l[0] = 53
tup = tuple(l)

print(tup)

print()
# Here l stores the values of tuple as a list
# after changing into list we can access the elements in a list....Here we accessed the element with index 0 which is 1 and we changed to 53 
# after we changed the list into tuple and stored in tuple
# so now the tuple prints like this (53, 0, 5, 2, 1, 8, 9, 23)

''' we can directly concatnate two tuples without changing into list
'''
countries = ("Finland","England","New Zeland")
countries1 = ("India","Hongkong","UAE")
bothcountries = (countries+countries1)
print(bothcountries)