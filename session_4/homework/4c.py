x = []

for i in range(1,10):
    for j in range (1,10):
            x.append(i*j)
    print (x, end = "\n")
    x = []

x = []
n = int(input("Enter your number: "))

for i in range(1,n+1):
    for j in range (1,n+1):
            x.append(i*j)
    print (x, end = "\n")
    x = []