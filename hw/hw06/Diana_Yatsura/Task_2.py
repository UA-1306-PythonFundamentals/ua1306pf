def check_login(l):
    login = 'First'
    while l != login:
        print('ERROR ERROR ERROR')
        break
    else:
        print(f"Hello, {login}!")
l = input('Enter your login ')
check_login(l)