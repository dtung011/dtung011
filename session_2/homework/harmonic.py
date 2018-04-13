n = int(input("Enter a number: "))

x = 1
for i in range (1,n+1):
    x = i*x

print (x)

t =1
for i in range (1,n+1):
    t = t + 1/i

print (t)