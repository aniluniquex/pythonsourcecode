def avg(*numbers):
    sum = 0
    #print(numbers) # it takes the numbers in the form of tuple
    for i in numbers:
        # print(i) # this code to refer what are the values of i
        sum = sum + i
    # print("The sum is:", sum / len(numbers))
    return sum / len(numbers)

c = avg(1,25)
print(c)

# here 1 and 25 are numbers took as tuple
# the value of i at first is 1 and after that it got increased by 25
