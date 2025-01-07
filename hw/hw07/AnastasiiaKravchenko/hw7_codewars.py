import math


def greet(name):
    """
    Jenny's secret message
    """
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)


def distance(x1, y1, x2, y2):
    """
    Find The Distance Between Two Points
    """
    return round(math.sqrt((x1 - x2)**2 + (y1 - y2)**2), 2)


def filter_words(st):
    """
    No yelling!
    """
    return ' '.join(st.capitalize().split())


def number_to_string(num):
    """
    Convert a Number to a String!
    """
    return str(num)


def reverse(st):
    """
    Reversing Words in a String
    """
    return ' '.join(st.split()[::-1])


def reverse_list(l):
    """
    Reverse List Order
    """
    return l[::-1]


def solution(number):
    """
    Multiples of 3 or 5
    """
    if number < 0:
        return 0
    sum = 0
    for n in range(1, number):
        if (n % 3 == 0) or (n % 5 == 0):
            sum += n
    return sum


def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    Will you make it?
    """
    gallons = distance_to_pump / mpg
    return fuel_left >= gallons


def are_you_playing_banjo(name):
    """
    Are You Playing Banjo?
    """
    if name.lower()[0] == 'r':
        return f'{name} plays banjo'
    return f'{name} does not play banjo'


def bool_to_word(boolean):
    """
    Convert boolean values to strings 'Yes' or 'No'.
    """
    if boolean:
        return "Yes"
    return "No"


def count_sheeps(sheep):
    """
    Counting sheep...
    """
    return sheep.count(True)


def correct_tail(body, tail):
    """
    Is this my tail?
    """
    return body[-1] == tail
