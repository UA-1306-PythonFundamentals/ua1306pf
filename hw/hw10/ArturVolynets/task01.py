# Task1. Create a polygon class and a rectangle class that inherits 
# from the polygon class and finds the square of rectangle.

class Polygon:
    '''
    A base class for polygons.
    '''
    def __init__(self) -> None:
        pass

class Rectangle(Polygon):
    '''
    A class representing a rectangle, inheriting from Polygon.
    '''
    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def area(self) -> float:
        '''
        Method to calculate the area (square) of the rectangle.
        '''
        return self.x * self.y

# rectangle = Rectangle(5, 3)
# print(f"The area of the rectangle is: {rectangle.area()}")

