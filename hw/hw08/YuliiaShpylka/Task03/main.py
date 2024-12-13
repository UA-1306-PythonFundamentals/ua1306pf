from calc_area import area_rectangle, area_triangle, area_circle

def user_input():
    user_input = input("""Please choose function for calculation:
1 - rectangle, 2 - triangle, 3 - circle: """)

    if int(user_input) == 1:
        lenght = input("Please eneter Lenght: ")
        width = input("Please enetr Width: ")
        print(area_rectangle(int(lenght), int(width)))
    elif int(user_input) == 2:
        base = input("Please eneter Base: ")
        hight = input("Please enter Hight: ")
        print(area_triangle(int(base), int(hight)))
    else:
        radius = input("Please eneter Radius: ")
        print(area_circle(int(radius)))

def main():
    user_input()

if __name__ == '__main__':
    main()

