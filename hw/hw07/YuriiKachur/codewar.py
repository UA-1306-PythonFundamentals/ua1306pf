#1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
#2
import math

def distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(d, 2)
#3
def filter_words(st):
    words = st.split()
    words = [words[0].capitalize()] + [word.lower() for word in words[1:]]
    return ' '.join(words)
#4
def number_to_string(num):
    return str(num)
#5
def reverse(st):
    return ' '.join(st.split()[::-1])

#6
def reverse_list(l):
    return l[::-1]

#7
def solution(number):
    if number < 0:
        return 0

    return sum(n for n in range(number) if n % 3 == 0 or n % 5 == 0)

#8
def zero_fuel(distance_to_pump, mpg, fuel_left):

    return mpg * fuel_left >= distance_to_pump

#9
def are_you_playing_banjo(name):
    if name.lower().startswith('r'):
        return name + " plays banjo"
    return name + " does not play banjo"

#10
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#11
def count_sheeps(sheep):
    return sum(1 for s in sheep if s)

#12
def correct_tail(body, tail):
    if body[-len(tail):] == tail:
        return True
    else:
        return False




