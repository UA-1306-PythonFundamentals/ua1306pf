from calculate_area import area_of_rectangle, area_of_triangle, area_of_circle

def main():
    shape = input("Please, choose and enter a shape: rectangle, triangle or circle ")

    if shape == 'rectangle':
        print(area_of_rectangle())
    elif shape == 'triangle':
        print(area_of_triangle())

    elif shape == 'circle':
        print(area_of_circle())

# print(main())

if __name__ == '__main__':
    main()