n = int(input("Enter number of rows: "))

print ("*"*n)

for i in range (2,n-1):
    print (" "*(n-i),"*"," "*(n-i-2),end="")
    print ("\n")

print ("*"*n)