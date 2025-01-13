import re


def password_validation(password):
    """
    Validates a password based on the following criteria:
    - Contains at least one digit.
    - Contains at least one lowercase letter.
    - Contains at least one uppercase letter.
    - Contains at least one special character ($, #, or @).
    - Length is between 6 and 16 characters.
    """
    if (re.search(r"[0-9]", password) and
            re.search(r"[a-z]", password) and
            re.search(r"[A-Z]", password) and
            re.search(r"[$#@]", password) and
            6 <= len(password) <= 16):
        return "Password is valid"
    return "Invalid password"
