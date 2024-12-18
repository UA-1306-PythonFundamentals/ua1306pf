import re

def validate_password(password):
    """Validate the password based on given criteria."""
    if (6 <= len(password) <= 16 and
        re.search(r'[a-z]', password) and
        re.search(r'[A-Z]', password) and
        re.search(r'\d', password) and
        re.search(r'[$#@]', password)):
        return True
    return False

def main():
    password = input("Enter a validate password: ")
    if validate_password(password):
        print("Password is valid.")
    else:
        print("Password is invalid. Make sure it meets the following criteria:")
        print("- At least one lowercase letter [a-z]")
        print("- At least one uppercase letter [A-Z]")
        print("- At least one digit [0-9]")
        print("- At least one special character from [$#@]")
        print("- Length between 6 and 16 characters")

if __name__ == "__main__":
    main()
