

def determine_day_of_week():
    try:
        
        user_input = input("Введіть число: ")
        number = int(user_input)  

        
        days_of_week = {
            1: "Понеділок",
            2: "Вівторок",
            3: "Середа",
            4: "Четвер",
            5: "П'ятниця",
            6: "Субота",
            7: "Неділя"
        }

        
        if 1 <= number <= 7:
            print("Це день тижня: " + days_of_week[number])
        elif number >= 8:
            print("Число більше 7. Днів тижня лише 7!")
        else:
            print("Число менше 1. Днів тижня лише 7!")

    except ValueError:
        print("Введено некоректне значення. Будь ласка, введіть ціле число.")


determine_day_of_week()