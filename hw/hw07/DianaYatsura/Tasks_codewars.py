# TASK 1. Jenny's secret message

# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return f"Hello, {name}!"
#
# TASK 2. Find The Distance Between Two Points

# def distance(x1, y1, x2, y2):
#     return round((((x2 - x1)**2 +(y2 - y1)**2)**0.5), 2)

# TASK 3. No yelling!

# def filter_words(st):
#     st = " ".join(st.capitalize().split())
#     return st

# TASK 4. Convert a Number to a String

# def number_to_string(num):
#     return str(num)

# TASK 5. Reversing Words in a String

# def reverse(st):
#     words = st.strip().split()
#     return ' '.join(reversed(words))

# TASK 6. Reverse List Order

# def reverse_list(l):
#     l.reverse()
#     return l
#
# print (reverse_list(l=[]))

# TASK 7. Multiples of 3 or 5

# def solution(number):
#     result = []
#     if number <= 0:
#         return 0
#     for n in range(number):
#         if n % 3 == 0 or n % 5 == 0:
#             result.append(n)
#     return sum(result)
#
# print(solution())

# TASK 8. Will you make it?

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     fuel_needs = distance_to_pump/mpg
#     if fuel_needs <= fuel_left:
#         return True
#     else:
#         return False

# print(zero_fuel(100, 50, 1))
#
# TASK 9. Are You Playing Banjo?

# def are_you_playing_banjo(name):
#     if name[0] == 'R' or  name[0] == 'r':
#         return f'{name} plays banjo'
#     else:
#         return f'{name} does not play banjo'
#
# print(are_you_playing_banjo(''))

# TASK 10. Convert boolean values to strings 'Yes' or 'No’

# def bool_to_word(boolean):
#         if boolean is True:
#             return 'Yes'
#         else:
#             return 'No'
#
# print(bool_to_word(True))

# TASK 11. Counting sheep

# def count_sheeps(sheep):
#     present = list(sheep).count(True)
#     return present
#
# print(count_sheeps([]))

# TASK 12. Is this my tail?

# def correct_tail(body, tail):
#     if body[-1]== tail:
#         return True
#     else:
#         return False
#
# print(correct_tail("Emu", "t"))