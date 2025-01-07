import re


def validate_password(string):
    if not (6 <= len(string) <= 16):
        return False

    if not re.search("[a-z]", string):
        return False

    if not re.search("[A-Z]", string):
        return False

    if not re.search("[0-9]", string):
        return False

    if not re.search("[$#@]", string):
        return False

    return True


def main():
    password = input("Enter your password: ")
    if validate_password(password):
        print("Password is valid.")
    else:
        print("Password is not valid.")


if __name__ == "__main__":
    main()
