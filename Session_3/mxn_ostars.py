m = int(input("Enter number of colummns: "))
n = int(input("Enter number of rows: "))

# print ("*" * n)

for i in range (n):
    for j in range (m):
        if (i+j) % 2 == 0:
            print ("*", end="")
        else:
            print ("o", end="")
    print ("\n")