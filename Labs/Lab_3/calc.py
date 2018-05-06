def calc(x,y,op):
    result = 0
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x / y
    return result

print (__name__)
if __name__ == "__main__":
# when the dictionary is ran directly, __name__ is __main, when it is ran in other files, __name__ returns to the name of the dictionary
    print("Calc imported")

# r = calc(1,2,"+")
# print (r)
