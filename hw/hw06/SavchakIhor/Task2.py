def check_login(user_input):
    login = 'First'
    if user_input == login:
        print(f"Hello, {login}!")
    else:
        print('Wrong credentials')


user_input = input('Enter your login: ')
check_login(user_input)