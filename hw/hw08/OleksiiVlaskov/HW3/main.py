from calc import area_circle, area_rectangle, area_triangle

def user_input():
    print("""This program can calculate the area of a rectangle, triangle and circle
    if you want to calculate:
    rectangle - enter 1;
    triangle - enter 2;
    circle - enter 3;""")
    user_input=input('Your choice: ')
    if user_input.isdigit() and int(user_input) <= 3:
        return user_input
    print('Enter number 1, 2 or 3')
        
def second_user_input(first_input):
    match (first_input):
        case '1':
            try:
                length, width = input("\nEnter length and width of the rectangle:\n").split()
                print(f"Area of the rectangle is: {area_rectangle(length=float(length),width=float(width))}")
            except Exception as e:
                print(f"Error: {e}")
        case '2':
            try:
                base, p_height = input("\nEnter base and perpendicular height of the triangle:\n").split()
                print(f"Area of the triangle is: {area_triangle(base=float(base),p_height=float(p_height))}")
            except Exception as e:
                print(f"Error: {e}")
        case '3':
            try:
                radius = input("\nEnter radius of the circle:\n")
                print(f"Area of the circle is: {area_circle(radius=float(radius))}")
            except Exception as e:
                print(f"Error: {e}")

def main():
    first_input=user_input()
    second_user_input(first_input)
    
if __name__ == '__main__':
    main()