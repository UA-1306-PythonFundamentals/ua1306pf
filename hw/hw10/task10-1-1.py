class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def number_of_sides(self):
        return len(self.sides)

class Rectangle(Polygon):
    def __init__(self, width, height):
        # Rectangle has 4 sides, we define it explicitly here
        super().__init__([width, height, width, height])
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height
