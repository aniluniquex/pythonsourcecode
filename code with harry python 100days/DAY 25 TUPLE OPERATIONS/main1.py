Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
# res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:',Tuple1.count(3))

print("The position of 3 is",Tuple1.index(3,4,7))

# see how position works is it checks the element from index 4 to (7-1) so the position of 3  is at index 5 in that range
# Note: It always gives the position of first occurance
