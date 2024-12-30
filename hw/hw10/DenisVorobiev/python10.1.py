class Polygon:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Rectangle(Polygon):
    def area(self):
        return self.length * self.width

# Пример использования:
rect = Rectangle(5, 3)
print("rectangle:", rect.area())