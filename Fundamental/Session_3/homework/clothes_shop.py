Items = ['T-shirt', 'Sweater']
n = (input("What do you want? C, U, D "))

#Create
if n == "R":
    print ("Our Items", (Items))
    New = (input("Enter new item: "))
    Items.append(New)
    print (Items)

#Update
if n == "U":
    print ("Our Items", (Items))
    Update = int(input("Update position: "))-1
    New = (input("Enter new item: "))
    Items[Update+1] = New
    print (Items)

#Delete
if n == "D":
    print ("Our Items", (Items))
    Delete = int(input("Enter delete position: "))-1
    Items.pop(Delete)
    print (Items)
