import calculator
import re

def select():
    request = input("enter area of what you want to find, triangle, rectangle, or circle:\n")
    if re.search(r'riang', request):
        print(calculator.tri_area())
    elif re.search(r'ircl', request):
        print(calculator.circ_area())
    elif re.search(r'ectang', request):
        print(calculator.rect_area())
    else:
        print("try typing better")
select()