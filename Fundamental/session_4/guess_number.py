from random import *

n = randint(0,100)
x = int(input("Enter ur number: "))
loop = True
wrongcount = 0

while loop:
    if x > n:
        print ("Too big")
        x = int(input("Enter again: "))
        wrongcount += 1
        if wrongcount > 8:
            loop = False
            print ("Bye Bye")
    elif x < n:
        print ("Too small")
        x = int(input("Enter again: "))
        wrongcount += 1
        if wrongcount > 8:
            loop = False
            print ("Bye Bye")
    else:
        print ("Bingo")
        loop = False