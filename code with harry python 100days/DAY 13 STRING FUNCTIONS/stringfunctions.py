a = "anilvarma"
b = "Harry Khan!!"
names = "shubjan rahil anil faf kohli"
aln = "hello123"
printable = "\nwhistle podu"
string = "      "
bookname = "Harry Potter"
capitals = "ANILISBOSS"
nnn = "sMALL boY"
title = "uniquex groups"
print(a.upper()) # THis converts the string into capital letters
print(a.lower()) #THis converts the string to small letters
print(b.rstrip("!")) # removes certain thing in a string
print(a.capitalize()) # This capitalise the first letter in a string
print(a.replace("anilvarma","ms dhoni")) # This will replace anilvarna abd prints ms dhoni
print(names.split(" ")) # This will split into diffrent things by using a certain property which we give in the brackets
print(a.center(50)) #makes things to the center
print(a.count("a")) # This prints no of a in string a
print(b.endswith("!")) # checks whether this endswith ! or not
print(a.endswith("il",0,4)) # checks within a limit of 0 and (4-1)
print(a.find("a")) # checks the position of a specific thing if not found it returns -1
print(b.index("K")) # check whether K present or not if it is presented it prints that specific position and if not it returns an error
print(aln.isalnum()) # checks whether a string contains letters and numbers
print(aln.isalpha()) # checks whether the string contains only alpha letters
print(aln.islower()) # checks whether the letters are small are not
print(printable.isprintable()) # checks whether it is printable or not if it is like "helloeevdv" then it is printable but when we use \n then it is escape character where it is not printable so it returns false
print(string.isspace()) # chcks whether there are spaces are not in a string
print(bookname.istitle()) 
# basically in titles after spaces there should be capital of the first word then it is considered as title so it checks whether it is title or not 
print(capitals.isupper()) # checks wheteher a string is is completely capital or not
print(capitals.startswith("ANIL")) 
print(nnn.swapcase()) #convert smaller case to upper and upper to smaller
print(title.title()) #converts the first letter of a word into capital