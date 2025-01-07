# def error_function():
#     raise ValueError()
#     print("Print from error_function")
#     return "String from error_function"

# def print_without_error():
#     print("Print from print_without_error")

# try:
#     print_without_error()
# except ValueError:
#     print("We caught ValueError")
# else:
#     print("Print from else")
#     print(error_function())
# finally:
#     print("End of try...except")

# print("End of program")


my_list = [1, 2, 3, 4, 5]

try:
    print(my_list[5])
except Exception:
    print("We caught Exception")
except IndexError:
    print("We caught IndexError")