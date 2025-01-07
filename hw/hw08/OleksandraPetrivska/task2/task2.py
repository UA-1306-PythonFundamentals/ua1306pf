import re

def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return "Password must be between 6 and 16 characters."
    
    if not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter [a-z]."
    
    if not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter [A-Z]."
    
    if not re.search("[0-9]", password):
        return "Password must contain at least one digit [0-9]."
    
    if not re.search("[$#@]", password):
        return "Password must contain at least one special character [$#@]."
    
    return "Password is valid!"


password = input("Enter your password: ")


result = validate_password(password)
print(result)

