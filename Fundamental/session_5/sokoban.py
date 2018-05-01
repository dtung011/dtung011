# Show map
loop = True
Px = 2
Py = 2
Bx = 1
By = 1
Gx = 0
Gy = 0
for y in range(4):
    for x in range(4):
        if x == 2 and y == 2:
            print ("P", end = " ")
        elif x == 1 and y == 1:
            print ("B", end = " ")
        elif x == 0 and y == 0:
            print ("G", end = " ")
        else:
            print ("_", end = " ")
    print()

while loop:
    #input command
    print()
    m = input("Your move? W/A/S/D: ")

    #Update map
    if m == "W":
        Py -= 1
        if Py < 0 or Py > 3:
            Py += 1
    elif m == "S":
        Py += 1
        if Py < 0 or Py > 3:
            Py -= 1
    elif m == "A":
        Px -= 1
        if Px < 0 or Px > 3:
            Px += 1
    elif m == "D":
        Px += 1
        if Px < 0 or Px > 3:
            Px -= 1

    if Px == Bx and Py == By:
        if m == "W":
            By -= 1
            if By < 0 or By > 3:
                Py += 1
                By += 1
        elif m == "S":
            By += 1
            if By < 0 or By > 3:
                Py -= 1
                By -= 1
        elif m == "A":
            Bx -= 1
            if Bx < 0 or Bx > 3:
                Px += 1
                Bx += 1
        elif m == "D":
            Bx += 1
            if Bx < 0 or Bx > 3:
                Px -= 1
                Bx -= 1

    if Bx == Gx and By == Gy:
        print ("you win!!!!")
        loop = False 
    else:
        for y in range(4):
            for x in range(4):
                if x == Px and y == Py:
                    print ("P", end = " ")
                elif x == Bx and y == By:
                    print ("B", end = " ")
                elif x == Gx and y == Gy:
                    print ("G", end = " ")
                else:
                    print ("_", end = " ")
            print()
        if Bx == 0 and By == 3 or Bx == 3 and By == 3 or Bx == 3 and By == 0:
            print ("you lose!!!")
            loop = False




