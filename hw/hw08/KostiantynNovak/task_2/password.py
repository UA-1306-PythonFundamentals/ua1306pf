import re

def new_password():
    new_pass = input("enter password:\n")
    if len(new_pass) < 6:
        print("must be longer short") 
    if len(new_pass) > 16:
        print("must be shorter")
    if not re.search("[a-z]", new_pass):
        print("must have small letters")
    if not re.search("[A-Z]", new_pass):
        print("must have big letters")
    if not re.search("[0-9]", new_pass):
        print("must have numbers")
    if not re.search("[$#@]", new_pass):
        print("must have special symbols")
    else:
        password = new_password
        print(f"New password set")
        return password

              
new_password()