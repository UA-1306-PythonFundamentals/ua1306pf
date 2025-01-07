import re


def check_password_validity(password):
    # Перевірка довжини пароля
    if len(password) < 6 or len(password) > 16:
        return "Invalid: Password length must be between 6 and 16 characters."
    
    # Перевірка наявності хоча б однієї літери [a-z]
    if not re.search("[a-z]", password):
        return "Invalid: Password must contain at least one lowercase letter (a-z)."
    
    # Перевірка наявності хоча б однієї літери [A-Z]
    if not re.search("[A-Z]", password):
        return "Invalid: Password must contain at least one uppercase letter (A-Z)."
    
    # Перевірка наявності хоча б одного числа [0-9]
    if not re.search("[0-9]", password):
        return "Invalid: Password must contain at least one number (0-9)."
    
    # Перевірка наявності хоча б одного символу [$#@]
    if not re.search("[$#@]", password):
        return "Invalid: Password must contain at least one special character ($, #, or @)."
    
    # Якщо всі умови виконані
    return "Valid password."


# Зчитування пароля від користувача
user_password = input("Enter your password: ")
print(check_password_validity(user_password))
