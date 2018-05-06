from random import *
from calc import calc

while True:
    x = randint(1,10)
    y = randint(1,10)
    list_err = [1,2,-1,-2,0,0,0,0,0,0,0]
    list_op = ["+", "-", "*", "/"]
    op = choice(list_op)
    err = choice(list_err)
    result = 0

    # if op == "+":
    #     result = x + y
    #     dis_re = result + err
    # elif op == "-":
    #     result = x - y
    #     dis_re = result + err
    # elif op == "*":
    #     result = x * y
    #     dis_re = result + err
    # elif op == "/":
    #     result = x / y
    #     dis_re = result + err

    result = calc(x,y,op)
    dis_re = result + err

    print ("{0}{1}{2} = {3}".format(x, op, y, dis_re))
    answer = input("Right or Wrong? R or W ").upper()
    diff = dis_re - result

    if answer == "R" and diff == 0:
        print()
        print ("Great!", end="/n")
    elif answer == "R" and diff != 0:
        print()
        print ("U r wrong!", end = "/n")
    elif answer == "W" and diff == 0:
        print()
        print ("U r wrong!", end = "/n")
    elif answer == "W" and diff != 0:
        print()
        print ("Great!", end = "/n")
    
    print()
    print ("Press Ctrl + C + Enter to exit")
    print()





