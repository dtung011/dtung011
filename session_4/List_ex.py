menu = ['pho', 'com rang', 'banh my', 'chao']
print (menu)

menu.append("hu tieu")
print (menu)

# For i
for i in range(len(menu)):
    print(menu[i])

# For each
for item in menu:
    print(item)

# For enum
for i, item in enumerate(menu):
    message = "{0}, {1}".format(i+1, item)
    print(i+1, ".", item)

