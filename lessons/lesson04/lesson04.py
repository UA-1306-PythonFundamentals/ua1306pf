# a = 1
# b = 2
# c = 2

# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)

# print(True, not True)
# print(False, not False)

# print(True and (True or  False and True))

# a = [1,2,3]
# b = [1,2,3]
# c = b

# print(id(a), a)
# print(id(b), b)
# print(id(c), c)
# print(f"{a==b =}")
# print(f"{a is b =}")
# print(f"{id(a) == id(b) =}")
# print(f"{b is c =}")
# print(f"{a is not b =}")


# text = """
# he Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested."""


# print("Zen" in text)
# print("A" in text)
# print("A" not in text)
# # print("A" in not text) #SyntaxError: invalid syntax
# # print("A" in 12) #TypeError: argument of type 'int' is not iterable

# l = [1, 2, 3, [4, 5]]

# print(1 in l)
# print(4 in l)
# print([4, 5] in l)
# print((4, 5) in l)

# a = int(input("age:"))
# print(a>5 and a<10)
# print(5 < a < 10)
# a, b, c, d = 1, 2, 3, 4
# print(a < b and b < c and c < d)
# print(a < b < c  < d)

# print(True and 55 and "test")
# print(True and [] and "test")
# print(0 or [] or "test" or 55)
# print(0 or [] or () or None)
# is_false = [False, None, 0, "", [], (), {}, set()]

# l = []
# if len(l)> 0:pass
# if l:pass


# score = int(input("score:"))

# if score > 8:
#     print("You have passed the exam")
#     print(f"you score:{score}")


# print("Exam was finished.")



# temperature = float(input('What is the temperature? '))
# if temperature > 30:
#     print('Wear shorts.')
# else:
#     print('Wear long pants.')

# print('Get some exercise outside.')



# age = int(input("age:"))

# if age < 12:
#     print('kid')
# elif age < 18:
#     print('teenager')
# elif age < 50:
#     print('adult')
# else:
#     print('you are not old')



# if age < 12:
#     print('kid')
# else:
#     if age < 18:
#         print('teenager')
#     else:
#         if age < 50:
#             print('adult')
#         else:
#             print('you are not old')


# l = "         "
# if l:
#     print(True)


# age = int(input("age:"))

# result = None
# if age < 50:
#     result = 'yong'
# else:
#     result = 'you are not old'

# print(result)


# result = 'yong' if age < 50 else 'you are not old'
# # result = age < 50 ? 'yong' : 'you are not old'


# print(result)

# status = int(input("status code:"))

# match status:
#     case 400:
#         print('Bad request')
#     case 401:
#         print('Unauthorized')
#     case 403:
#         print('Forbidden')
#     case 404:
#         print('Not found')
#     case _:
#         print('Other error')

# print("end")

# match status:
#     case 400:
#         print('Bad request')
#     case 401 | 403 as error:
#         print(f'{error} is authentication error')

#     case 404:
#         print('Not found')
#     case _:
#         print('Other error')


# values = input("comands: ").split()
# print(f"{values=}")
# match values:
#     case "load", link:
#         print(f"load {link=}")
#     case "save", link, filename:
#         print(f"save {link=}, {filename=}")
#     case "save", link, *filenames:
#         print(f"save {link=}")
#         for filename in filenames:
#             print(f"\t{filename=}")
#     case _:
#         print("defoult", values)


# def funk():
#     print("test")

# ma = {
#     "key": funk
# }

# ma["key"]()
a = input("text: ")
if "x" in a:
    b = 25

print(b)
