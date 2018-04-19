print ("Choose a number from 0-100 and answer my question")
loop = True
x = 50
numchain = [0,50,100]

while loop:
    print (x)
    n = (input("is your number: b for Bigger, s for Smaller and e for Equal my number?"))
    if n == "b":
        numchain.append(x)
        numchain.remove(min(numchain))
        x =(x + max(numchain))//2
        print (x)
    elif n == "s":
        numchain.append(x)
        numchain.remove(max(numchain))
        x = (x + min(numchain))//2
        print (x)
    elif n == "e":
        print ("Yeah, I made it!!")
        loop = False
    