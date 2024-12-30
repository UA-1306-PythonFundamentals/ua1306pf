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
        raise ValueError("Number must be between 1 and 7.")

    return days_of_week[number]


def main():
    while True:
        try:
            user_input = input("Enter a number (1-7) to get the day of the week: ")
            number = int(user_input)  # Convert input to integer
            day = get_day_of_week(number)
            print(f"The day of the week is: {day}")
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number between 1 and 7.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

        # After an invalid input, the user will be prompted to enter a new number
        print("Try again.")


if __name__ == "__main__":
    main()
