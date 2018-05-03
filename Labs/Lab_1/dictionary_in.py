person = {
    "name": "Quan",
    "age": 22,
    "gender": "undefined",
    "address": "Hanoi",
    "login_count": 7
}

# if "name" in person:
#     print("Yeah")
# if "name" in person.keys():
#     print ("Yeah")

# if "address" in person.keys():
#     print ("found")
# else:
#     print ("Not found")

print(person.values())
if "Quan" in person.values():
    print("We found him")