from re import search

def regex_validation(input_string):
    reg_check=search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*[$#@])', input_string)
    if not reg_check == None and 6<=len(input_string)<=16:
        return('Password is valid')
    return('Password is not valid')