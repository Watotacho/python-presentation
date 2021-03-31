s="Sarah is my friend"
print(s)
print("Sarah is \n my friend")#insert new line
print("Sarah is \v my friend")#add vertical tab
a="software"
print(a.upper())#capitalize all character
print(a.lower())#turn all character of string to lower case
print(a.title())#capitalize the first letter of each word in a string
print(a.capitalize())#capitalize the first letter of a string
first_name="Isacko"#insert data in to string template before output
county="Malindi"
print(f"Good morning {first_name} ,am from {county} Kenya")
s="1,2,3,4,5"
print(s.index("3"))#it is exclusive of the last word in index position
print(s.index("2"))
print(s[2:3])
names=["James","Wendy","Sarah","Teresa","Angela"]
print(names[0:3])#it is exclusive of the last word in index position
print(names[1:4])
names.append("Stella")#add an item to the bottom of a list
print(names)
names.insert(2,"Constant")#it insert constant before index position
print(names)
names.sort()#arrange items in ascending order
print(names)
cheeses = ["Gouda", "Swiss", "Provolone", "Cheddar"]#transverse a list of items
for cheese in cheeses:
    print(cheese)






