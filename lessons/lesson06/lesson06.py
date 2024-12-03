# list

# l = list()
# print(type(l), l)
# # l = list(67) #TypeError: 'int' object is not iterable
# l = list("987654")
# print(type(l), l)
# l = []
# print(type(l), l)
# l = ["987654", 1, 2, 3, 4]
# print(type(l), l)

# l[0] = "test"
# print(type(l), l)
# matrix = [
#     [1, 2, 3],
#     [3, 4, 5],
#     [6, 7, 8]
# ]
# print(matrix)
# for row in matrix:
#     print(row)
# for row in matrix:
#     for e in row:
#         print(e, end="\t")
#     print()

# row_2 = matrix[1]
# print(row_2)
# row_2[1] = "test"

# for row in matrix:
#     for e in row:
#         print(e, end="\t")
#     print()

# matrix.append(5)
# print(matrix)
# for row in matrix:
#     if type(row) in (list, tuple):
#         for e in row:
#             print(e, end="\t")
#         print()
#     else:
#         print(row)

# n = matrix[3]
# print(n)
# n = 15
# print(n, matrix)

# print(matrix[0][2])

# l = [1,2,3,4]
# print(l)
# l.append(l)
# print(l)
# print(l[1])
# print(l[4][4][4][4][4][4][4][4][4][4][4][4][4][4][4][4][4])
# print(l[-2])
# print(l[1:3])

# l1 = [1, 2, 3]
# l2 = [1, 2, 3]
# l3 = [3, 2, 1]
# print(f"{l1 == l2=} ")
# print(f"{l1 is l2=} ")
# print(f"{l1 == l3=}")
# print(f"{l1 is l3=}")

# print(dir(list))

# print([method for method in dir(list) if not method.startswith("_")])
# l=[1,2,3]
# print(l)
# l.append("text")
# print(l)
# l.append(10)
# l.append(l)
# print(l)
# # l.extend(1)#TypeError: 'int' object is not iterable
# l.extend("text")
# print(l)
# l.extend(l)
# print(l)
# l.insert(5,99)
# print(l)
# l.insert(999,999)
# l.insert(-999,-999)
# # print(list(enumerate(l)))
# print(l)
# print(l.remove(3))
# l.remove("t")
# l.remove("t")
# l.remove("t")
# l.remove("t")
# # l.remove("t") #ValueError: list.remove(x): x not in list
# l.remove("text")
# print(l)
# element = l.pop()
# print(element, l)
# element = l.pop(10)
# print(element, l)
# # element = l.pop(100) #IndexError: pop index out of range

# def my_s(element):
#     if type(element) not in (int, float):
#         # print(element, len(element))
#         return len(element)
#     return element

# l.sort(key=my_s)
# print(l)
# ll = sorted(l, key=lambda e: -len(e) if type(e) not in (int, float) else -e)
# print(l)
# print()
# print(ll)
# print(l)
# l.reverse()
# print(l)
# ll = l[::-1]
# print(l, ll)
# ll = reversed(l)
# print(l, ll)
# print(l.count(1))
# print(l.count(11))
# # print(l.index(11))#ValueError: 11 is not in list
# l.append(2)
# print(l)
# print(l.index(2))
# print(l.index(2, 5))
# print(l.index(2, 7))
# # print(l.index(2, 7, 12)) #ValueError: 2 is not in list


# l1 = [1,2,3,4]
# l2 = [5,6]
# l3 = [l1, l2, 7, 8]

# print(l1)
# print(l2)
# print(l3)
# l1.clear()
# l2 = [99,88,77]
# print(">"*20)
# print(l1)
# print(l2)
# print(l3)


# l1 = [1, 2, 3, 4]
# l2 = [5, 6]
# l3 = [l1, l2, 7, 8]

# print(id(l3), l3)
# l4 = l3.copy()
# l4 = l3[:]
# print(id(l4), l4)
# l3[0][2]=99
# l3[2]=77
# print(id(l3), l3)
# print(id(l4), l4)

# from copy import deepcopy
# l5 = deepcopy(l3)
# l3[1][0]="text"
# l3[3]="google"
# print(id(l3), l3)
# print(id(l5), l5)


# from copy import copy
# a = [1, 2]
# b = Kooo(a)


# all() Return True if all elements of the list are true (or if the list is empty).
# any() Return True if any element of the list is true. If the list is empty, return False.
# enumerate() Return an enumerate object. It contains the index and value of all the items of list as a tuple.
# len() Return the length (the number of items) in the list.
# list() Convert an iterable (tuple, string, set, dictionary) to a list.
# max() Return the largest item in the list.
# min() Return the smallest item in the list
# sorted() Return a new sorted list (does not sort the list itself).
# sum() Return the sum of all elements in the list.

# a = [1, 2, 43, 5, "a", [1, 2]]
# print(all(a))
# a = [1, 2, 43, 0, "a", [1, 2]]
# print(all(a))
# # print(all(1))#TypeError: 'int' object is not iterable

# a = [False, 0, None, "", []]
# print(any(a))
# a = [False, 0, None, "", [1]]
# print(any(a))
# print(list(enumerate(a)))
# print(len(a))
# print(a.__len__())

# print(max([1,2,3,4]))
# print(max(["1","2","3","4"]))
# print(max(["1",2,"3","4"], key=lambda x: x if type(x) is int else 0))
# a = ["11","2","13","4"]
# print(sorted(["11","2","13","4"]))
# print(a)
# print(sum([1,2,3,4.5]))

# a = [1, 2, 43, 5, "a", [1, 2]]

# print(dir())
# del a
# a = [1, 2, 43, 5, "a", [1, 2]]
# b = a
# print(dir())
# del b
# print(dir())
# del a[0]
# print(a)
# del a[0:3]
# a = [1, 2, 43, 5, "a", [1, 2]]
# del a[1:4:2]
# print(a)


## tuple

# l = tuple()
# print(type(l), l)
# l = tuple("bdsjfbdjgb")
# print(type(l), l)
# l = ()
# print(type(l), l)
# l = (1, 2, 3)
# print(type(l), l)
# l = ("1")
# print(type(l), l)
# l = ("1",)
# print(type(l), l)

# t = ("a", 1,2,3,[1])
# print(t)
# print(t[1])
# print(t[0:2])
# # t[0] = 15#TypeError: 'tuple' object does not support item assignment
# t[-1].append(55)
# print(t)
# # print([method for method in dir(list) if not method.startswith("_")])
# print([method for method in dir(tuple) if not method.startswith("_")])

# print(t.count(1))
# print(t.count(0))
# print(t.index(1))
# print(t.index(1, 5, 9))

# from random import randint


# l = list(randint(0, 9999999999) for _ in range(9999))
# t = tuple(l)
# print(l.__sizeof__())
# print(t.__sizeof__())


# # set
# s = set()
# print(type(s), s)

# s = set("sasasddafdadsadsadsadsasdadasasd")
# print(type(s), s)

# s = {}  # <class 'dict'> {}
# print(type(s), s)
# s = {1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 4, 3, 2, 1, 2}
# print(type(s), s)

# print([method for method in dir(set) if not method.startswith("_")])
# s = set("abcdefg")
# print(s)
# s.add("z")
# s.add("zzz")
# print(s)
# s.update("zzpr")
# print(s)
# # s.add([1,2,3])#TypeError: unhashable type: 'list'
# s.add((1,2,3))

# print(s)
# s.add((1,2,3, [1])) #TypeError: unhashable type: 'list'
# def hash_str(text):
#     result = 0
#     for c in text:
#         result += ord(c)
#     return result%100

# print(hash_str("abc"))
# print(hash_str("abc"))

# print("aaa".__hash__())

# print(s)
# print(s.pop())
# print(s)

# # print(s.remove('1')) #KeyError: '1'
# print(s.remove('a'))
# print(s)

# print("a" in s)
# print("f" in s)

# a = set("asbjfbadsjfbdsljfbkdsujbvjfd")
# print(a)
# for e in a:
#     print(e)

# print(list(enumerate(a)))
# print(sorted(a))

# fs = frozenset(a)
# print(fs)


# dict

# d = {}
# print(type(d), d)

# d = {
#     "key": "value",
#     1566: "test",
#     (1,2,3): "test2",
#     # (1,2,3,[]): "test2", #TypeError: unhashable type: 'list'
#     }
# print(type(d), d)

# d = dict()
# print(type(d), d)

# # d = dict("sadf") #ValueError: dictionary update sequence element #0 has length 1; 2 is required
# # d = dict([[1,2], ["a", "aa"], ["ab", "ab","b" ]])#ValueError: dictionary update sequence element #2 has length 3; 2 is required
# print(type(d), d)


# d = {
#     "key": "value",
#     1566: "test",
#     (1, 2, 3): "test2",
#     "d": {
#         "9key": "d_value",
#         91566: "d_test",
#         (91, 2, 3): "d_test2",
#     },
# }
# print(d)

# # print(d[1])#KeyError: 1
# print(d["key"])
# print(d[1566])
# print(d[(1, 2, 3)])
# print(d["d"])
# print(d["d"][91566])

# d = {
#     "key": "value",
#     "dicts": [{j*i: j+i for i in range(1,5) } for j in range(1,3)]
# }
# from pprint import pprint
# pprint(d, width=3)

# d["key2"] = 99
# pprint(d, width=3)
# print([method for method in dir(dict) if not method.startswith("_")])
# d = {
#     "key": "value",
#     1566: "test",
#     (1, 2, 3): "test2",
#     "d": {
#         "9key": "d_value",
#         91566: "d_test",
#         (91, 2, 3): "d_test2",
#     },
# }
# print(d)

# dd = d.fromkeys("abcd", "Test")
# print(dd)
# print(d.get("key"))
# print(d.get("key33"))
# print(d.get("key33", 0))
# print(d.get("key", 0))
# print(d)
# # print(d.pop()) #TypeError: pop expected at least 1 argument, got 0
# print(d.pop("key")) #TypeError: pop expected at least 1 argument, got 0
# print(d)
# dd = d.setdefault("abcd", {
#     "key44": "value",
#     15: "test",
#     }) 
# # dd = d["abcd"]= 99 
# print(dd)
# print(d)
# d.update({
#     "key44": "value",
#     15: "test",
#     })

# print(d)
# 
# print(d.keys())
# print(d.values())
# print(d.items())

# print("key" in d)
# print("test" in d)

# for key in d:
#     print(f"{key}\t{d[key]}")

# # a, b = (1, 8)
# for key, value in d.items():
#     print(f"{key}\t{value}")


# d = {
#     "key": "value",
#     "1566": "test",
#     "(1, 2, 3)": "test2",
#     "d": {
#         "9key": "d_value",
#         91566: "d_test",
#         (91, 2, 3): "d_test2",
#     },
# }
# print(sorted(d))


print([i for i in range(5)])
print({i for i in range(5)})
print({i:i*i for i in range(5)})
print((i for i in range(5)))