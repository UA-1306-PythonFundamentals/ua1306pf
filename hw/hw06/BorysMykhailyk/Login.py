while True:
    user_input = input("Enter login: ") 

    # Перевірка чи введене число є додатнім цілим, та наявність команди на вихід з циклу
    if user_input=='First':
        print("Access granted. Welcome")
        break
    else:
        print("Error: wrone login")