while True:
    login = input("Please enter your login: ")
    if login == "First":
        print(f"Welcome {login}! Nice to see you.")
        break
    else:
        print("Error: Invalid login. Please try again.")
