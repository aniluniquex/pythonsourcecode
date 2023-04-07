# saying good morning using time module



import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
timestamphour = time.strftime("%H")
print(timestamp)
timestampminute = time.strftime("%M")
print(timestamp)
timestampsec = time.strftime("%S")
print(timestamp)

if(int(timestamphour)>0 and int(timestamphour)<12):
    print("Good morning")
elif(int(timestamphour)>=12 and int(timestamphour)<18):
    print("Good afernoon")
else:
    print("Good Evening")