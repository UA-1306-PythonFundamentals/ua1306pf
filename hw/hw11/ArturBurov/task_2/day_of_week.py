def get_day_of_week(day_number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday",
    }
    if day_number in days:
        return days[day_number]
    else:
        return "Invalid day number. Please enter a number between 1 and 7."


def main():
    try:
        day_number = int(input("Enter a day number (1-7): "))
        day_name = get_day_of_week(day_number)
        print(day_name)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()