password = input("Enter password: ")
minLength = 8
while len(password) < minLength:
    print("Password is must be atleast", minLength, "characters")
    password = input("Enter password: ")

print("*"*len(password))