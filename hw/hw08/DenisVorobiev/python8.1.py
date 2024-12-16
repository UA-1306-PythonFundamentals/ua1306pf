import re

def check_password_validity(password):
    if (re.search(r'[a-z]', password) and
            re.search(r'[A-Z]', password) and
            re.search(r'[0-9]', password) and
            re.search(r'[$#@]', password) and
            6 <= len(password) <= 16):
        print("your password is correct")
    else:
        print("your password is not correct, pls use a-z, A-Z, 0-9, $#@, 6-16")

password = input("You password: ")
check_password_validity(password)

