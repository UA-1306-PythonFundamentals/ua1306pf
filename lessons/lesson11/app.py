# a = int(input("a: "))
# b = int(input("b: "))
# try:
#     print(a / b)
# except:
#     print("Error")
# print("end")



# # Program to handle multiple errors with one except statement
# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
# # note that braces () are necessary here for multiple exceptions
# # except(ZeroDivisionError, NameError, ValueError):
# #     print("Error Occurred and Handled")
# # print("end")

# except ValueError:
#     print("Value Error!")
# except NameError:
#     print("NameError!")
# except ZeroDivisionError:
#     print("ZeroDivisionError!")
# except Exception as err:
#     print("error", type(err), err)
# except:
#     print("Error!")
# else:
#     print("Nothing went wrong")
#     print("Value of b = ", b) 

# finally:
#     print("finally")

# def f():
#     try:
#         print("try start")
#         return 10
#         print("try end")
#     finally:
#         print("finally")
#         return 25

# print(f())

# def input_int(text):
#     data = input(text)
#     if not data.isdigit():
#         raise ValueError("That is not a positive number!")
#     return int(data)

# try:
#     value = input_int("Enter a positive integer: ")
# except ValueError as e:
#     print(e)

# input_int("test")
from loger import logging

class CustomError(Exception):
    pass


def input_int(text):
    data = input(text)
    if not data.isdigit():
        logging.error("That is not a positive number!")
        raise CustomError("That is not a positive number!")
    return int(data)

try:
    value = input_int("Enter a positive integer: ")
except CustomError as e:
    print(e)