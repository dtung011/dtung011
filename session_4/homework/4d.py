x = []

for i in range(10):
    for j in range(10):
        if (i+j) % 2 == 0:
            v = 1
        else:
            v = 0
        x.append(v)
    print (x, end = "\n")
    x = []

n = int(input("Enter your number: "))

for i in range(n):
    for j in range(n):
        if (i+j) % 2 == 0:
            v = 1
        else:
            v = 0
        x.append(v)
    print (x, end = "\n")
    x = []