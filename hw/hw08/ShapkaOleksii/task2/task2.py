has_lowercase = False
has_uppercase = False
has_digit = False
has_special_char = False

password = str(input("Enter the password: "))
if len(password) >= 6 and len(password) <= 16:
    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif char in "#$@":
            has_special_char = True
else:
    print("Invalid length! ")
if has_digit and has_uppercase and has_special_char and has_lowercase :
    print("Valid password ")
else :
    print("Invalid password ")