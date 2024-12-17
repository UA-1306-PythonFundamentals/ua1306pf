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


class User:
    # singl = None

    # def __new__(cls, *args, **kwargs):
    #     print("__new__", cls)
    #     if cls.singl is None:
    #         cls.singl = object.__new__(cls)
    #     print("__new__",  id(cls.singl))
    #     return cls.singl
        
    def __init__(self, name, age=18, email="test@in.ua"):
        print("__init__",  id(self))
        print("__init__", name, age, email)
        self.name = name
        self.age = age
        self.email = email

    def __del__(self):
        print("deleted", self)

    def __str__(self):
        return f"name:{ self.name} age:{self.age} email:{self.email}"

# user = User()
# print(type(user), user)
user1 = User("Liubomyr")
user2 = User("Oleh", 43, "oleh43@gmail.com")
print(id)
print(User)
print(user1 is user2)
# del user1
# print(dir())
print(user1)
print(user2)

