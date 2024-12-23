class Polygon:
    def __init__(self, sides):
        self.sides = sides  # List of sides

    def get_sides(self):
        return self.sides

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        super().__init__([length, breadth, length, breadth])  # Rectangle has 4 sides
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

# Example Usage
rectangle = Rectangle(5, 3)
print("Sides of rectangle:", rectangle.get_sides())
print("Area of rectangle:", rectangle.calculate_area())