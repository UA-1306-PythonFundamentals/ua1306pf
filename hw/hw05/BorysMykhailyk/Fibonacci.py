while True:
    print("\nTo stop program print 'end'") # Умова виходу з вічного циклу
    user_input = input("Enter ordinal number of Fibonacci number: ") 
    # Перевірка чи введене число є додатнім цілим, та наявність команди на вихід з циклу
    if user_input=='end':
        print("Goodbye)")
        break
    if not user_input.isdigit():
        print("Only positive integer allowed")
        continue
    # Визначення числа на протібній позиції
    num_input=int(user_input)

    x=0
    n0=0
    n1=1
    while x < num_input:
        n2=n1+n0
        n0, n1 = n1, n2
        x = x +1
    print(f"The {num_input}-th Fibonacci number is {n0}")
