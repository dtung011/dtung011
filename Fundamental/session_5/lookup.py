teencode = {"vc": "vai cut", "oc": "oc cho", "dm": "dau ma"}

while True:
    print (*teencode.keys())
    i = input("Enter your teencode: ")
    if i in teencode:
        print (teencode[i])
    else:
        YN = input("do you want to add a teencode? Y/N ")
        if YN == "Y":
            teencode[i] = input("Enter your meaning: ")
        elif YN == "N":
            print()