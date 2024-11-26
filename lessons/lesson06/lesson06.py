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

print([method for method in dir(list) if not method.startswith("_")])
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


l1 = [1, 2, 3, 4]
l2 = [5, 6]
l3 = [l1, l2, 7, 8]

print(id(l3), l3)
l4 = l3.copy()
l4 = l3[:]
print(id(l4), l4)
l3[0][2]=99
l3[2]=77
print(id(l3), l3)
print(id(l4), l4)

from copy import deepcopy
l5 = deepcopy(l3)
l3[1][0]="text"
l3[3]="google"
print(id(l3), l3)
print(id(l5), l5)
