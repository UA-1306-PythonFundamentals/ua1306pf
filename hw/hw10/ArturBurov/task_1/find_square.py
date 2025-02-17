class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides  # Number of sides
        self.sides = [0 for i in range(no_of_sides)]  # Initialize sides list

    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)  # Initialize with 2 sides (length and width)

    def findArea(self):
        a, b = self.sides
        area = a * b
        print('The area of the rectangle is %0.2f' % area)


rect = Rectangle()
rect.inputSides()
rect.dispSides()
rect.findArea()
