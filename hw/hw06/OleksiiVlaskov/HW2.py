login=False
while not login:
    user=input("Enter your login:\n")
    if user == 'First':
        login=True
        print(f"Welcome {user}")
    else:
        print('Wrong login please try again')