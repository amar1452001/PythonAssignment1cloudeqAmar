#Creating a complex dictionary and traverse through it

#DICTIONARY - Key:Value pairs, Unordered, Mutable

#Creating a Dictionary 

dic1={"name":"amarjot",
    "id":12, 
    "addr":"mohali", 
    "ls":[1,2,3,4],
    "tup": (5,6,7,8), 
    "d1":{"key":"value","k2":"v2", "key3":3}}

print(dic1)

#printing type of variable named as "dic1"
print(type(dic1))

#adding elements in dictionary
dic1["4th key"] = "four"

print(dic1)

#deleting a key 
del(dic1["id"])

#TRAVERSING through the dictionary

for key,value in dic1.items():
    print(key,value)

print(dic1.items())

for key in dic1:
    print(key) #gives the key
    print(dic1[key]) #gives the values

#ACCESSING nested element in dictionary
print(dic1["tup"][2])

