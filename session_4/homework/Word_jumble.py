from random import choice

print ("Guess the world below: ")
Words = ["hawaii", "government", "corporate", "swear", "masterpiece", "venison", "happiness", "dinosaur"]

loop = True

while loop:
    x = choice(Words)
    t = list(x)
    Words.remove(x)
    for i in range(len(t)):
        y = choice(t)
        print (y, end =" ")
        t.remove(y)
    answer = input("\n Your answer is: ")
    if answer == x:
        print ("Great job!")
        loop = False
    else:
        print ("Try again")
    Next = input("Do you want to continue? Yes or No? \n ")
    if Next == "Yes":
        loop = True
    elif Next == "No":
        print ("Bye Bye")
        loop = False

    