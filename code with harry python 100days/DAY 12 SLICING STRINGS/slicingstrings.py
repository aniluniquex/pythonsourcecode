a = "Anilvarma"

print(len(a))

print(a[0:8]) # it prints anilvarm
# the first num before : denotes the starting point and it prints upto n-1 of last number which is present after :

print(a[:9]) # if we omitt that it actually takes as 0 at start
print(a[1:6]) # it prints from 1 to 5
print(a[-1:-4]) # it prints empty line because we can print from 8:5

print(a[-4:-1]) # it prints arm
print(a[len(a)-4:len(a)-1]) # actually the derivation or clear explaination is this one
