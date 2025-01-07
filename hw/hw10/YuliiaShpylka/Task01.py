class Polygon:

    def __init__(self, width, high):
        self.width = width
        self.high = high


class Rectangle(Polygon):

    def square(self):
        s = self.width * self.high
        return f"Rectangle square is: {s}"


square1 = Rectangle(1,5)
print(square1.square())



