#linear search is an algorithm that looks for each member of a list, respectively.

nums = [3, 4, -98, 88, 9, 3]

x = int(input("Enter an interger: "))

for num in nums:
    if num == x:
        print("found")
        break
else:
    print ("not found")

#If for runs smoothly, without any break -> run to else