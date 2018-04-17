# List - CRUD: Create - Read - Update - Delete.

#To seperate list
names = ["Canh", "Hieu", "Duc Anh"]
print (*names, sep =", ")

#append
new_name = input("Enter your name: ")
names.append(new_name)
print (*names, sep =", ")

#set variable
names[1] = "Hieu Dep Trai"

#Loop for limited list
for i in range (len(names)):
    print (names[i])
print()

#Foreach loop
for i in names:
    print(i)
print()


