class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"x:{self.x} y:{self.y}"
    def __repr__(self):
        return f"({self.x}, {self.y})"
    def __add__(self, other):
        p3 = Point()
        p3.x = p1.x+p2.x
        p3.y = p1.y+p2.y
        return p3
    def __lt__(self, other):
        return self.dist_to_zero() > other.dist_to_zero()
    
    def dist_to_zero(self):
        return (self.x**2 + self.y**2)**0.5
    
    def print(self):
        print(self)
    # def print(self, x):
    #     print(self, x)

p1 = Point(5, 8)
print(p1.dist_to_zero())
p2 = Point(3, -7)
p = [p1, p2]
print(p1)
print(p2)
print(p)
# p3 = Point()
# p3.x = p1.x+p2.x
# p3.y = p1.y+p2.y
p3 = p1 + p2
print(p3)
p.append(p3)
print(p)
p.sort()
# p.sort(key= lambda x: x.dist_to_zero())
print(p)

# p1.print(1)

from pprint import pprint
pprint(Point.__dict__)