import math


def greet(name):
    """
    Jenny's secret message: A special greeting for Johnny.
    """
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"


def distance(x1, y1, x2, y2):
    """
    Calculate the distance between two points (x1, y1) and (x2, y2).
    """
    return round(math.sqrt((x1 - x2)**2 + (y1 - y2)**2), 2)


def filter_words(st):
    """
    Capitalize the first word of the sentence and remove extra spaces.
    """
    return ' '.join(st.capitalize().split())


def number_to_string(num):
    """
    Convert a number to a string.
    """
    return str(num)


def reverse(st):
    """
    Reverse the order of words in a string.
    """
    return ' '.join(reversed(st.split()))


def reverse_list(l):
    """
    Reverse the order of elements in a list.
    """
    return l[::-1]


def sum_of_multiples(number):
    """
    Find the sum of all multiples of 3 or 5 below the given number.
    """
    if number < 0:
        return 0
    return sum(n for n in range(1, number) if n % 3 == 0 or n % 5 == 0)


def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    Determine if you can reach the pump with the remaining fuel.
    """
    return fuel_left * mpg >= distance_to_pump


def are_you_playing_banjo(name):
    """
    Determine if someone whose name starts with 'R' or 'r' plays banjo.
    """
    return f"{name} plays banjo" if name.lower().startswith('r') else f"{name} does not play banjo"


def bool_to_word(boolean):
    """
    Convert boolean values to strings 'Yes' or 'No'.
    """
    return "Yes" if boolean else "No"


def count_sheeps(sheep):
    """
    Count the number of True values in the list (sheep present).
    """
    return sheep.count(True)


def correct_tail(body, tail):
    """
    Check if the tail matches the last character of the body.
    """
    return body.endswith(tail)
