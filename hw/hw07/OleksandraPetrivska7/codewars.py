#1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#2
def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)

#3
def filter_words(st):
    st = " ".join(st.split()).capitalize()
    return st

#4
def number_to_string(num):
    return str(num)

#5
def reverse(st):
    words = st.split(' ') 
    st = ' '.join(reversed(words)) 
    return st

#6
def reverse_list(l):
    'return a list with the reverse order of l'
    l.reverse()
    return(l)

#7
def solution(number):
    result = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)

    return sum(result)
  

#8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

#9
def are_you_playing_banjo(name):
    first = name[0]
    if first == "r" or first == "R":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

#10
def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    if boolean == False:
        return 'No'

#11
def count_sheeps(sheep):
    return sum(bool(x) for x in sheep)

#12
def correct_tail(body, tail):
    sub = body[len(body)-1:len(body)]
    if sub == tail:
        return True
    else:
        return False

