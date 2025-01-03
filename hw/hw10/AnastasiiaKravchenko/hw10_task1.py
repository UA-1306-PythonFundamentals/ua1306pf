class Polygon:
    def __init__(self, *args):
        self.sides = args

    def __repr__(self):
        return f'Polygon of {len(self.sides)} sides'


class Rectangle(Polygon):
    def __init__(self, *args):
        super().__init__(*args)

    def square(self):
        a, b = self.sides
        return a * b


r = Rectangle(3, 5)
print(r)
print(r.square())
