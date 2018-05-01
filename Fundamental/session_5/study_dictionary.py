# person = ["Quan", 40, "single", "Hanoi", 2, 11]
# print (person)

# Khai bao dictionary thu nhat
# person = {}
# print (person)

# person = {"name": "Quan"}
# print (person)

#An dictionary includes 2 things: key and value
# Key must be in string typye, use ""

#To access a member of a dictionary: dictionary["key"]

person = {"name": "Quan",
        "age": 40}

#Doi bien
person["age"] = 22

print (person["age"])

# If key in dictionary: true or false
i = input("Enter your query: ")
if i in person:
        print (person(i))
else:
        print (i, "in not dictionary")

del person["age"]

for key, value in person.items():
        print(key, ":", value)
