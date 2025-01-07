class Not_in_range(Exception):
    pass

def entered_number_analyzer(number):
    day_of_the_week=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    try:
        number=int(number)
        if 0<number<8:
            return f"{day_of_the_week[number-1]}"
        else:
            raise Not_in_range("The number must be in the range from 1 to 7")
    except ValueError as e:
        return "Next time, enter a natural number"
    except Not_in_range as e:
        return f"Error: {e}"
    
print(entered_number_analyzer('6'))
print(entered_number_analyzer(4))
print(entered_number_analyzer(0))
print(entered_number_analyzer('as'))
