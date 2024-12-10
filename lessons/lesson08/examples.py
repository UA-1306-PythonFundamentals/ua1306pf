# import constants
# import temp

# import sys
# from pprint import pprint
# pprint(sys.path)

# file = open("data.txt")
# # sys.path.append("c:\\data\\github\\ua1306pf")
# # from lessons.lesson05.lesson05 import s

# import p.app3 as pa3
# pa3.a
# import p.app3
# p.app3.a

# print(dir())
# from constants_copy import *
# print(dir())
# print(dir())
# from constants_copy import __a, _a
# print(dir())
import constants_copy
print(constants_copy.age )
print(constants_copy._a )
print(constants_copy.__a )


class A():
    def __init__(self):
        self.a =1
        self._a =2
        self.__a =3
    def __str__(self):
        return f"{self.a} {self._a} {self.__a} "
    
a = A()
print(a)
print(a.a)
print(a._a)
print(a._A__a)