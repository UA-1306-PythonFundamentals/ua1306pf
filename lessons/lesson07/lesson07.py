# def my_sum(a, b):
#     print(f"{a}+{b}={a+b}")

# my_sum(1, 5)
# print(my_sum)

# print(sum([1,2,3,4,5]))

# s = sum
# print(s([1,2,3]))
# sum = my_sum
# sum(15, 12)

# def sum(a, b, c):
#     return (a, b, c)

# print(sum(1,2,33))

# def f():pass

# print(f())
# def f():
#     return 1

# print(f())

# def f():
#     return

# print(f())

# help(print)

# print(print.__doc__)

# def f():
#     """thi funk
#     return a
#     """
#     pass

# help(f)
# print(f.__doc__)
# def my_f(a, b):
#     s = 0
#     for i in range(a, b):
#         s += i
#         print(i)
#         if s > 10:
#             return s


# print(my_f(1, 100))
# print(my_f(1, -100))


# def print_info(name):
#     print(name)

# # print_info()#TypeError: print_info() missing 1 required positional argument: 'name'
# # print_info("liubomyr", 38) #TypeError: print_info() takes 1 positional argument but 2 were given
# print_info("liubomyr")


# def print_info(name, age):
#     print(f"{name=}")
#     print(f"{age=}")

# print_info("liubomyr", 38)


# def print_info(name, age=18):
#     print(f"{name=}")
#     print(f"{age=}")

# print_info("liubomyr")
# print_info("liubomyr", 38)

# def f(a, b, c=1, d):
#     pass

# def f(l=[]):
#     l.append(1)
#     print(l)
# f([1,2,3])
# f([10, 20])
# f()
# f()
# f()
# f([10, 20])
# f()


# def print_info(name, age=18, city="Biberka"):
#     print(f"{name=}")
#     print(f"{age=}")

# print_info("liubomyr", 38)
# print_info(38, "liubomyr")
# print_info(age=38, name="liubomyr")
# print_info(age=38, name="liubomyr")
# print_info("taras", city="odesa", age=20)
# # print_info(age=20, "taras", city="odesa")
# # print_info("taras", 12,  age=22)


# def f(a, b, *args, c=1, d="test", **kwargs):
#     print(f"{a=} {b=} {args} {c=} {d=} {kwargs}")

# f(1,2)
# f(1,2,3,4,5,6,7,8,9,10,  c=1, d=1, e=1,k=1 )

# f(1,2,nane="13")


# def f(a, b, c, d, e, *args, **kwargs):
#     print(f"{a=} {b=} {c=} {d=} {e=} {args=} {kwargs}")
#     return a + b + c + d + e

# l = [1,2,3,4,5]
# print(f(l[0], l[1], l[2], l[3], l[4]))
# print(f(*l))

# d = {
#     "a":10,
#     "b":40,
#     "c":30,
#     "f": 999,
#     "d":40,
#     "e":50,
# }

# print(f(*d))
# print(f(**d)) 


# print(dir())
# # print(dir(int))
# # print(int.__dict__)

# def f():
#     print(dir())

# print(dir())
# f()



# def scope_func():
#     print(x)
#     # x = 10
#     print("Value inside function:", x)

# x = 20

# scope_func()
# print("Value outside function:", x)




# def scope_func():
#     global x
#     print(x)
#     x = 10
#     print("Value inside function:", x)

# x = 20

# scope_func()
# print("Value outside function:", x)


# def o():
#     def i():
#         pass
#     pass

# def number(n):

#     def a_add_number(a):
#         nonlocal n
#         n += a
#         print(f"{n=}")
#         return a_add_number
#     return a_add_number


# n3 = number(3)
# n3(5)
# n3(5)
# n4 = number(4)
# n4(5)
# n3(5)

# number(50)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)(5)





# def fac(n):
#     result = 1
#     for i in range(1,n+1):
#         result *=i
#     return result

# print(fac(5))

# # import sys
# # sys.setrecursionlimit(10000)
# def r_fac(n):
#     # print(f"{n=}")
#     if n <= 0:
#         print(f"{n=}")
#         return 1
#     else:
#         print(f"{n}*r_fac({n-1}) ")
#         return n*r_fac(n-1) 
    
# print(r_fac(5))

def name(a, b):
    return a+b

name = lambda a,b: a+b
print(name(1,2))
l = [1,2,6,4,3, "test", (1,2,4), {"a": 3}]
l.sort(key=lambda x: x if type(x) in [int, float] else len(str(x)) )
print(l)
l.sort(key=lambda x: x if type(x) in [int, float] else sum(x.values()) if type(x) is dict else len(str(x))  )
print(l)
