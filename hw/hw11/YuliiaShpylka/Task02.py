def days_of_week(number):
    days = {
        1: "Monday",
        2: "Tuesday", 
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"}
    
    try:
        number.isdigit()
        if not int(number) in days:
           raise KeyError()
    except ValueError:
        return(f"Entered value is not number")
    except KeyError:
        return(f"Entered number is out of scope")
    else:
        x = days[int(number)]
        return(f"This is {x}")

def main():
    user_input = input("Please enter day number: ")
    result = days_of_week(user_input)
    print(result)

if __name__ == "__main__":
    main()
 