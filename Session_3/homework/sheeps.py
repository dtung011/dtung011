#Max sheep size
print ("My best sheep size:")
Sheeps = [5,7,300,90,24,50,75]
print (max(Sheeps))

#Sheep size after the maximum one is sheared
print ("My sheeps sizes after being sheared:")
Sheeps[Sheeps.index(max(Sheeps))] = 8
print (Sheeps)

#Sheeps size in the next 4 months
print ("Month 1:")
for i in range (len(Sheeps)):
    Sheeps[i] = Sheeps[i] + 50
print (Sheeps)

print ("Month 2:")
for i in range (len(Sheeps)):
    Sheeps[i] = Sheeps[i] + 50
print (Sheeps)

print ("Month 3:")
for i in range (len(Sheeps)):
    Sheeps[i] = Sheeps[i] + 50
print (Sheeps)

print ("Month 4:")
for i in range (len(Sheeps)):
    Sheeps[i] = Sheeps[i] + 50
print (Sheeps)

#Total money after selling my sheeps;
print ("My revenue: ")
amount = sum(Sheeps)
print (amount*2)