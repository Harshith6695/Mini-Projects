# Password Strength Checker

password = input("Enter password: ")

if len(password) < 6:
    print("Too Short Password")
elif password.isalpha():
    print("Weak Password")
elif password.isalnum():
    print("Strong Password")
else:
    print("Invalid Password")
