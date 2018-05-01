from getpass import getpass

u = getpass("Enter your username: ")

if u == "c4e":
    p = getpass("Enter your password: ")
    if p == "code the change":
        print ("Welcome!")
    else: 
        print ("your password is wrong")
else:
    print ("your username is wrong")