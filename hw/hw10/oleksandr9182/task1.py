class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_sides(self):
        return f"Багатокутник з {self.sides} сторонами."


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(sides=4)  
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height



if __name__ == "__main__":
   
    rect = Rectangle(width=5, height=3)  

    
    print(rect.display_sides())  
    print(f"Ширина: {rect.width}, Висота: {rect.height}")  
    print(f"Площа прямокутника: {rect.area()}") 
