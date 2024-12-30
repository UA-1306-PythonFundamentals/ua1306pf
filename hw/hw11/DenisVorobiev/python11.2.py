def get_day_of_week(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    if number < 1 or number > 7:
        return "enter 1 and 7."
    return days[number]

try:
    number = int(input("Enter a number 1-7: "))
    print(get_day_of_week(number))
except ValueError:
    print("Error: Please enter 1 - 7.")