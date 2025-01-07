import re

def validate_password(password):
    if re.fullmatch(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}', password):
        return "Valid Password."
    return "Invalid Password."

# Input from the user
password = input("Enter your password: ")
print(validate_password(password))