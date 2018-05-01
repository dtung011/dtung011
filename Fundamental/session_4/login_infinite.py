from getpass import getpass

loop = True
wrong_count = 0

u = getpass("Enter your username: ")

if u == "c4e":
    while loop:
        p = getpass("Enter your password: ")
        if p == "code the change":
            print ("Welcome!")
        else: 
            wrong_count += 1
            print ("your password is wrong")
            if wrong_count >= 3:
                loop = False
                print ("Bye Bye")
else:
    print ("your username is wrong")
    