import re


def is_valid_pass(user_pass):
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,16}$"
    return re.match(password_regex, user_pass)


user_password = input('Enter your password:\n')
if is_valid_pass(user_password):
    print('Valid password!')
else:
    print('Error: invalid password!')
