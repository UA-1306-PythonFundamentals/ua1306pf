import re

pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,16}$')

password = input("Enter your password: ")

if pattern.match(password):
    print("Valid Password")
else:
    print("Invalid Password")
