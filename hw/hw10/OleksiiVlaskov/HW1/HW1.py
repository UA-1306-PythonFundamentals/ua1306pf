class Polygon:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        __pwd__ = a
        
class Rectangle(Polygon):
    def square(self):
        return f"square of rectangle is: {self.a * self.b}"
    
    
        
a = Rectangle(2,5)
print(a.square())