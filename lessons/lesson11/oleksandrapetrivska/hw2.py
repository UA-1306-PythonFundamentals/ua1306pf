class InvalidDayError(Exception):
    pass

def get_day_of_week(number):
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    if number < 1 or number > 7:
        raise InvalidDayError("The number must be between 1 and 7.")
    
    return days_of_week[number]

def get_number_from_user():
    while True:
        try:
            user_input = input("Please enter a number (1-7) to get the corresponding day of the week: ")
            
            number = int(user_input)
            
            day = get_day_of_week(number)
            
            print(f"The corresponding day of the week is: {day}")
            break  
            
        except ValueError:
            print("Error: Please enter a valid number (1-7).")
        except InvalidDayError as e:
            print(e)

get_number_from_user()

