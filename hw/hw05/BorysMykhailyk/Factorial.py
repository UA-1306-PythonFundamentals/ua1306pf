# Копія коду із завдання на пошук чисел Фібоначі
while True:
    print("\nTo stop program print 'end'") # Умова виходу з вічного циклу ()
    user_input = input("Enter number: ") 

    # Перевірка чи введене число є додатнім цілим, та наявність команди на вихід з циклу
    if user_input=='end':
        print("Goodbye")
        break
    if not user_input.isdigit():
        print("Only positive integer allowed")
        continue
# Пошук факторіала числу без застосування рекурсії
    num_input=int(user_input)
    factorial=1
    for i in range(1, num_input+1):
        factorial=factorial*i
    print(factorial)