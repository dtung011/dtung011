numbers = [1,6,8,1,2,1,5,6]

#Use count
x = int(input("Enter a number: "))
message = "{0} appears {1} times in numbers".format(x, numbers.count(x))
print (message)

#Not use count
x = int(input("Enter a number: "))
t = 0
for i in range(len(numbers)):
    if numbers[i] == x:
        t +=1
message = "{0} appears {1} times in numbers".format(x, t)
print (message)