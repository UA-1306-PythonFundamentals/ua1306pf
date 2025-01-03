
def check_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним")
    
    if age % 2 == 0:
        return "парним"
    else:
        return "непарним"


try:
    age_input = input("Будь ласка, введіть ваш вік: ")
    age = int(age_input)
    result = check_age(age)
    print("Ваш вік " + str(age) + " є " + result + " числом")
except ValueError as e:
    if str(e) == "Вік не може бути від'ємним":
        print(e)
    else:
        print("Помилка: число не ціле")