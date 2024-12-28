# class User(object):

# class User:
#     """class for user"""
#     pass



# u = User()

# print(User)
# print(u)

# print(type(u) is User)



# class User:
#     ci = 10
#     cm = [20]

#     def __init__(self):
#         self.ii = 10
#         self.im = [9]

#     def print(self):
#         print(self.ci, self.cm, self.ii, self.im)

# u1 = User()
# u2 = User()

# print(u1,u1.ci, u1.cm, u1.ii, u1.im)
# print(u2,u2.ci, u2.cm, u2.ii, u2.im)

# u1.ii = 99
# u2.im.append("test")
# u2.cm.append("Class")
# print(u1,u1.ci, u1.cm, u1.ii, u1.im)
# print(u2,u2.ci, u2.cm, u2.ii, u2.im)

# print(dir(u1))
# print(dir(User))
# print(u1.__dict__)
# print(User.__dict__)
# u1.print()
# u2.print()

# f = User.print

# f(u1)


# def super_print(obj):
#     print(type(obj), obj)

# super_print(u1)

# User.sp = super_print
# u2.sp()


# class User:
#     # singl = None

#     # def __new__(cls, *args, **kwargs):
#     #     print("__new__", cls)
#     #     if cls.singl is None:
#     #         cls.singl = object.__new__(cls)
#     #     print("__new__",  id(cls.singl))
#     #     return cls.singl
        
#     def __init__(self, name, age=18, email="test@in.ua"):
#         print("__init__",  id(self))
#         print("__init__", name, age, email)
#         self.name = name
#         self.age = age
#         self.email = email

#     def __del__(self):
#         print("deleted", self)

#     def __str__(self):
#         return f"name:{ self.name} age:{self.age} email:{self.email}"

# # user = User()
# # print(type(user), user)
# user1 = User("Liubomyr")
# user2 = User("Oleh", 43, "oleh43@gmail.com")
# print(id)
# print(User)
# print(user1 is user2)
# # del user1
# # print(dir())
# print(user1)
# print(user2)



# class OBJ:
#     ci = 10
#     cm = [20]

#     def __init__(self, ii=10, im=None):
#         self.ii = 10
#         self.im = [9] if im is None else im

#     def __str__(self):
#         return f"ci:{self.ci} cm:{self.cm} ii:{self.ii} im:{self.im}"
    
#     def set_ci(self, ci):
#         # OBJ.ci = ci
#         self.__class__.ci = ci
    
#     @classmethod
#     def set_c_ci(cls, ci):
#         # OBJ.ci = ci
#         cls.ci = ci

# obj1 = OBJ(5, [1,2,3])
# obj2 = OBJ(50, [121,2,3])
# print(obj1)
# print(obj2)
# obj1.ii = 55
# obj2.im.append(99)
# # obj1.ci = 88
# # obj1.set_ci(88)
# # OBJ.set_ci(obj2, 999)

# # OBJ.set_c_ci("test")
# obj1.set_c_ci("test")
# obj2.cm.append("test")
# print(obj1, obj1.__dict__)
# print(obj2, obj2.__dict__)
# print(OBJ.cm, OBJ.ci)

# class A:
#     def __init__(self, a = 0):
#         self.a = a
#         self._a = a*2
#         self.__a = a*3
#     def __str__(self):
#         return f"{self.a} {self._a} {self.__a} "


# a = A(5)
# print(a.a)
# print(a._a)
# # print(a.__a)#AttributeError: 'A' object has no attribute '__a'. Did you mean: '_a'?
# print(a._A__a)
# print(a)



# class xrange:
#     def __init__(self, start, end=None, step=1):
#         self.start = start
#         self.end = end
#         self.step = step


# print(xrange(5))
# print(xrange(5, 10))
# print(xrange(5, 10, 2))

from multipledispatch import dispatch

@dispatch(int, int)
def add(a, b):
    return a + b

@dispatch(str, int)
def add(a, b):
    return a*b

print(add(5, 8))
print(add("5", 8))


