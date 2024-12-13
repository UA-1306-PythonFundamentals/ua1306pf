import re

def check_validity_password(password):
    errors = []
    if len(password) < 6 or len(password) > 16:
        errors.append('Password should contain 6 - 16 characters')
    if not re.search('[a-z]', password):
        errors.append('Password should  contain at least 1 lowercase letter')
    if not re.search('[A-Z]', password):
        errors.append('Password should  contain at least 1 uppercase letter')
    if not re.search('[0-9]', password):
        errors.append('Password should  contain at least 1 digit')
    if not re.search('[$#@]', password):
        errors.append('Password should  contain at least 1 special character')
    if errors:
        return 'Invalid password:\n' + '\n'.join(errors)
    return 'Valid password'

password = input('Please, enter your password ')
valid_password = check_validity_password(password)
print(valid_password)