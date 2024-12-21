from re import search

def pasword_validation(input_user):
    reg_val = search("[0-9]", input_user)
    reg_lower_case = search("[a-z]", input_user)
    uper_case = search("[A-Z]", input_user)
    simbols = search("[$#@]", input_user)
    if reg_val and reg_lower_case and uper_case and simbols and 6<=len(input_user)<=16:
        message = "Password is valid"
        return message
    else:
        error_mess = "Invalid password"
        return error_mess

    
    

