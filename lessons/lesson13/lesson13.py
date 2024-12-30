# l = [x * x for x in range(10)]
# print(l)
# l = [(x, y, x**y) for x in range(10) for y in range(10) if x < y]
# print(l)
# l = []
# for x in range(10):
#     for y in range(10):
#         if x < y:
#             l.append((x, y, x**y))
# print(l)

# l1 = [1,2,3]
# l2 = ["a", "b"]
# l3 = ["test", 25, 35, 45]
# print(list(zip(l1, l2)))
# print(zip(l3, l2))
# print(list(zip(l3, l2, l1)))


# def my_print(text):
#     return f">>{text}<<"

# l3 = ["test", 25, 35, 45]

# print(list(map(my_print, l3)))


# from functools import reduce




# def a_add_b(a, b):
#     print(f"{a=} {b=} {a+b=}")
#     return a+b
# print(reduce(a_add_b, [47,11,42,13]))
# print(reduce(a_add_b, [47,11,42,13], -99))

# l = [1,2,3,4,5]
# i = iter(l)
# print(i)
# print(next(i))
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# for i in range(10):
#     if i ==5 :
#         raise StopIteration()
#     print(i)
# print("end")


# class my_range:
#     def __init__(self, start, end=None, step=1):
#         if end is None:
#             self.start = 0
#             self.end = start
#         else:
#             self.start = start
#             self.end = end
#         self.step = step
#         self.current = None
#     def __repr__(self):
#         return f"My_range({self.start}, {self.end}, {self.step}, {self.current}) "
#     def __iter__(self):
#         self.current = self.start
#         print("__iter__", self)
#         return self
#     def __next__(self):
#         x = self.current
#         self.current += self.step
#         print("__next__", self)
#         if x > self.end:
#             raise StopIteration("my")
#         return x


# print(my_range(10))
# print(my_range(5, 10))
# print(my_range(5, 20, 3))

# for i in my_range(10):
#     print(i)

# print([i for i in range(5)])
# print((i for i in range(5)))
# n = 5
# l = [i**i for i in range(n)]
# t = (i**i for i in range(n))

# print(f"{n=} l({l.__sizeof__()}) t({t.__sizeof__()})")
# n = 50
# l = [i**i for i in range(n)]
# t = (i**i for i in range(n))
# print(f"{n=} l({l.__sizeof__()}) t({t.__sizeof__()})")
# n = 500
# l = [i**i for i in range(n)]
# t = (i**i for i in range(n))
# print(f"{n=} l({l.__sizeof__()}) t({t.__sizeof__()})")
# n = 5000
# l = [i**i for i in range(n)]
# t = (i**i for i in range(n))
# print(f"{n=} l({l.__sizeof__()}) t({t.__sizeof__()})")

# def my_g(n):
#     yield n+1
#     yield n+2
#     yield n+3

# g = my_g(5)
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def xrange(start, end=None, step=1):
#         if end is None:
#             start, end = 0, start
#         while start < end:
#              print("before yield", locals())
#              yield start
#              print("after yield", locals())
#              start += step
# for i in xrange(5):
#      print(">> ", i)
#      print("="*20)


# def print_star(funk):
#     def inner(*args, **kwargs):
#         print("*"*10)
#         funk(*args, **kwargs)
#         print("*"*10)
#     return inner

# def add(a,b):
#     print(a, b, a+b)

# add(5, 3)

# dadd = print_star(add)
# dadd(5, 3)

# add = print_star(add)

# @print_star
# def d(a,b):
#     print(a, b, a/b)

# d(5, 8)



# def print_star(funk):
#     print(f"{funk.__name__} {id(funk)}")
#     def inner(*args, **kwargs):
#         print("*"*10)
#         funk(*args, **kwargs)
#         print("*"*10)
#     print(f"dec {inner.__name__} {id(inner)}")
#     return inner

# @print_star
# def my_d(a,b):
#     print(a, b, a/b)

# my_d = print_star(my_d)


# print(f"{my_d.__name__} {id(my_d)}")

# def print_star(funk):
#     print(f"{funk.__name__} {id(funk)}")
#     def inner(*args, **kwargs):
#         print("*"*10)
#         result = funk(*args, **kwargs)
#         print("*"*10)
#         return result
#     print(f"dec {inner.__name__} {id(inner)}")
#     return inner

# @print_star
# def my_d(a,b):
#     print(a, b, a/b)
#     return a/b

# my_d = print_star(my_d)


# print(f"{my_d.__name__} {id(my_d)}")

def print_star(ch, in_line):
    def print_star(funk):
        print(f"{funk.__name__} {id(funk)}")
        def inner(*args, **kwargs):
            print(ch*in_line)
            result = funk(*args, **kwargs)
            print(ch*in_line)
            return result
        print(f"dec {inner.__name__} {id(inner)}")
        return inner
    return print_star



@print_star(ch="*", in_line=50)
def my_d(a,b):
    return a/b

@print_star(ch="<<", in_line=9)
@print_star(ch=">>", in_line=5)
def add(a,b):
    return a+b


print(my_d(5, 9))

add(8, 8)

d = {}
def disp(*params):
    global d
    def decorator(fun):
        d[params] = fun
        def inner(*args, **kwargs):
            t = tuple(map(type,args))
            result = d[t](*args, **kwargs)
            return result
        return inner
    return decorator


@disp(str, str)
def add(a, b):
    return a+b
print(d)
@disp(int, int)
def add(a, b):
    return a*b
print(d)

print(add("a", "b"))
print(add(5, 7))