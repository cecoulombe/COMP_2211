phoneBook = {"Bob": "250-828-1000", "Jane" : "250-828-2000"}
name = input("Enter a name: ")
if name in phoneBook:
    print(phoneBook[name])
else:
    print("Name not found.")