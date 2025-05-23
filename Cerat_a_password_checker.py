password = input("Enter a password: ")
minimum_number = 8

if len(password) <= minimum_number:
    print("Password is to short!!")
elif not any(char.isdigit() for char in password):
    print("Password must be contain at lest one number..")
elif not any(char in "@#$" for char in password):
    print("Enter a at least one special character...")
else:
    print("password is Valid...")