# class Point:
#     def __init__(self, x=0, y=0):
#         print("Point.__init__")
#         self.x = x
#         self.y = y
#     def __str__(self):
#         print("Point.__str__")
#         return f"x:{self.x} y:{self.y}"
#     def __repr__(self):
#         print("Point.__repr__")
#         return f"({self.x}, {self.y})"
#     def __add__(self, other):
#         print("Point.__add__")
#         p3 = Point()
#         p3.x = p1.x+p2.x
#         p3.y = p1.y+p2.y
#         return p3
#     def __lt__(self, other):
#         print("Point.__lt__")
#         return self.dist_to_zero() > other.dist_to_zero()

#     def dist_to_zero(self):
#         print("Point.dist_to_zero")
#         return (self.x**2 + self.y**2)**0.5

#     def print(self):
#         print("Point.print")
#         print(self)
#     # def print(self, x):
#     #     print(self, x)

# p1 = Point(5, 8)
# print(p1.dist_to_zero())
# p2 = Point(3, -7)
# p = [p1, p2]
# print(p1)
# print(p2)
# print(p)
# # p3 = Point()
# # p3.x = p1.x+p2.x
# # p3.y = p1.y+p2.y
# p3 = p1 + p2
# print(p3)
# p.append(p3)
# print(p)
# p.sort()
# # p.sort(key= lambda x: x.dist_to_zero())
# print(p)

# # p1.print(1)

# from pprint import pprint
# pprint(Point.__dict__)


# class Point3D(Point):
#     def __init__(self, x=0, y=0, z=0):
#         print("Point3D.__init__")
#         super().__init__(x, y)
#         self.z = z
#     def __str__(self):
#         # return super().__str__() + f" z:{self.z}"
#         return f" x:{self.x} y:{self.y} z:{self.z}"

# p3d = Point3D(3, 5)
# print(type(p3d), p3d, p3d.__dict__)

# print(p3d.dist_to_zero())

# print(type(p3d) is Point)
# print(isinstance(p3d, Point))
# print(type(p3d) in Point.__mro__)

# class Point4D(Point3D): pass
# p4d = Point4D()
# print(isinstance(p4d, Point))
# print(isinstance(p4d, Point3D))
# print(issubclass(Point4D, Point))


def f(func):
    def inner(*args, **kwargs):
        # print(args, kwargs)
        print(f"run func {func.__name__} {args} {kwargs}")
        func(*args, **kwargs)
    return inner

class Point:
 
    def __init__(self, x=0, y=0):
        print("Point.__init__")
        self.__x = x
        self.__y = y

    def __str__(self):
        print("Point.__str__")
        return f"x:{self.__x} y:{self.__y}"

    def __repr__(self):
        print("Point.__repr__")
        return f"({self.__x}, {self.__y})"
    @f
    def get_x(self):
        # print(f"get value for x {self.__x}")
        return self.__x
    @f
    def set_x(self, x):
        # print(f"set new value for x {x}")
        self.__x = x

    x = property(get_x, set_x)

    @property 
    @f
    def y(self):
        # print(f"get value for y {self.__y}")
        return self.__y
    @y.setter
    @f
    def y(self, y):
        # print(f"set new value for y {y}")
        self.__y = y

p = Point(15, 22)
print(p)
# p.set_x(55)
print(p.get_x())
print(p.x)
p.x = 88
p.y = 77
print(p.y)


    

f(1)
f("test")