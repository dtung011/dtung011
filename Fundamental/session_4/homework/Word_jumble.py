from random import choice

print ("Guess the world below: ")
Words = ["hawaii", "government", "corporate", "swear", "masterpiece", "venison", "happiness", "dinosaur", "hutchison", "singapore", "golden gate", "fortunately", "malaria"]

loop = True
x = choice(Words)
Words.remove(x)
t = list(x)

while loop:
    for i in range(len(t)):
        y = choice(t)
        print (y, end =" ")
        t.remove(y)
    answer = input("\n Your answer is: ")
    if answer == x:
        print ("Great job!")
        loop = False
        Next = input("\n Do you want to continue? Yes or No? \n ")
        if Next == "Yes":
            x = choice(Words)
            t = list(x)
            loop = True
        elif Next == "No":
            print ("Bye Bye")
            loop = False
    else:
        loop = True
        print()
        hint = input("Do you want a hint? Yes/No")
        if hint == "Yes":
            print ("The two first letter of the word are: ", x[0], x[1])
        else:
            print ("Try again")
        

    

    