class Shape:
    '''
    A base class for all shapes.
    '''
    def __init__(self) -> None:
        pass

    def area(self) -> float:
        '''
        Method to calculate the area of the shape.
        This is a placeholder, meant to be overridden in subclasses.
        '''
        raise NotImplementedError("Subclasses must implement this method")


class Polygon(Shape):
    '''
    A base class for polygons, inheriting from Shape.
    '''
    def __init__(self) -> None:
        super().__init__()

    # Other general polygon methods could go here.


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


# Example usage:
rectangle = Rectangle(5, 3)
print(f"The area of the rectangle is: {rectangle.area()}")
