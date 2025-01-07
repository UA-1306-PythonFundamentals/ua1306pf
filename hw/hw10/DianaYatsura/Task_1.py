class Polygon:

    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

    def which_shape(self):
        if self.number_of_sides == 3:
            print("Triangle")
        elif self.number_of_sides == 4:
            print("Rectangle")
        else:
            print('Polygon')

    def area(self):
        return "No Area"

    def perimeter(self):
        return "No Perimeter"


class Rectangle(Polygon):

    def __init__(self, width, length):
        super().__init__(4)
        self.width = width
        self.length = length

    def area(self):
        print(self.length * self.width)

    def perimeter(self):
        print(2 * (self.length + self.width))

a = Rectangle(5, 6)
a.area()
a.perimeter()