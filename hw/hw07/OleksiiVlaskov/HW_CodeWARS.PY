import math
#1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)
#2 
def distance(x1, y1, x2, y2):
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 2)
#3
def filter_words(st):
    st = st.capitalize()
    return ' '.join(st.split())
#4
def number_to_string(num):
    return str(num)
#5
def reverse(st):
    st=st.split()
    st=" ".join(str(o) for o in st[::-1])
    return st
#6
def reverse_list(l):
    'return a list with the reverse order of l'
    return l[::-1]
#7
def solution(number):
    result=0
    for n in range(3,number):
        if n >=3 and n%3 == 0:
            result += n
            print(f"{result=}{n=}")
        elif n >= 3 and n%5 == 0:
            result += n
            print(f"{result=}{n=}")
    return result
#8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump > mpg * fuel_left:
        return False
    return True
#9
def are_you_playing_banjo(name):
    if name[0].upper() == 'R':
        return name + " plays banjo" 
    return name + " does not play banjo"
#10
def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    return 'No'
#11
def count_sheeps(sheep):
    result=sheep.count(True)
    return result
#12
def correct_tail(body, tail):
    if tail == body[-1]:
        return True
    return False