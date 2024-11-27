# x = 'foo'
# y = x
# print (x, id(x)) # foo
# print (y, id(y)) # foo
# y += 'bar'
# print (f"{x=}", id(x)) # foo
# print (f"{y=}", id(y)) # foobar


# x = [1, 2, 3]
# y = x
# print (x, id(x)) # [1, 2, 3]
# print (y, id(y)) # [1, 2, 3]
# y += [3, 2, 1]
# print (f"{x=}", id(x)) # [1, 2, 3, 3, 2, 1]
# print (f"{y=}", id(y)) # [1, 2, 3, 3, 2, 1]

# a = int(10)
# print(type(a) is int)
# print(type(a) is str)
# print(isinstance(a, int))
# print(isinstance(a, str))

# print(">"*50)
# a = "test"

# print(type(a) is int)
# print(type(a) is str)
# print(isinstance(a, int))
# print(isinstance(a, str))


# print(">"*50)
# class A:pass
# class B(A):pass
# b = B()

# print(type(b) is A)
# print(type(b) is B)
# print(isinstance(b, A))
# print(isinstance(b, B))

# i = ZeroDivisionError()
# print(isinstance(i, ArithmeticError))
# print(isinstance(i, ZeroDivisionError))
# print(isinstance(i, AssertionError))


# a = 3 + 4 + 5 + 6 + 7 + 8 + 9
# print(a)

# a = 3 + 4 + 5 +\
#       6 + 7 + 8 + 9
# print(a)

# a = 3 + 4 + 5 
# + 6 + 7 + 8 + 9
# print(a)

# a = (3 + 4 + 5 + 
#      6 + 7 +
#        8 + 9)
# print(type(a), a)

# a = [3 + 4 + 5 +
     
#       6 + 7 +
#         8 + 9]
# print(a)

# print(
#     1, 2, 3, 4, 5,
#       sep="55",
#       end="==============="
# )


# print("1"); print(2)
# a, b, c = 1, 2, 3

# for i in range(2,6):
#     print(i)
#     print(str(i)*i)
# print("end")
# print(sum)
# print(sum([1,2,3,4]))
# sum = 15
# print(sum)
## print(sum([1,2,3,4]))#TypeError: 'int' object is not callable

# a, b, c = 1, 2, 3
# print(a,b,c)
# a, b, c = c, b, a
# print(a,b,c)

# MY_NAME = "Liubomyr"
# print(MY_NAME)
# MY_NAME = 1
# print(MY_NAME)


# a = 85
# print(a)
# a = 0b1010101 # 01
# print(a)
# a = 0o125 # 01234567
# print(a)
# a = 0x55 # 0123456789abcdef
# print(a)
# a = 0x10 # 0123456789abcdef
# print(a)

# a = 10000000000000000000
# a = 10_000_000_000_000_000_000
# print(a)

# f = 12.5
# print(f)
# f = 12.
# print(f)
# f = .5
# print(f)

# f = 15e5
# print(f)

# f = 15e-5
# print(f)

# print(10 + True)
# print(10**False)

# a = None
# # print(a)
# # a = Nill
# # print(a)

# l = [1, None, "test", 1.5]
# print(l)
# print(l[2])
# l[1] = 555 
# print(l)

# l = (1, None, "test", 1.5)
# print(l)
# print(l[2])
# print(l[2][::-1])
# print(l)

# print({1,2,3,4,51,2,3,1,2,3,2,3,2,3,2,3})
# print(set("sbf lkjcsdngljhs/adnbfvkdhawbesdlhjfhwabjef ueakjgf873hgf87wqy3hfgp87wyfhG87G978"))


# d = {
#     "KEY1": "valee",
#     12: {
#         "key": 15
#     },
#     55: 555
# }
# print(d)
# print(d[55])
# print(d["KEY1"])
# print(d[12])
# import sys
# sys.set_int_max_str_digits(999999)
# a = 999 ** 9999
# print(len(str(a)))


# s = str(d)
# print(s.upper())

# f = 35
# code = """a=35
# b = a * f
# print(a, b, f)
# """

# # exec(code)

# l = [1,2,3]
# print(l)
# t = tuple(l)
# print(t)
# print(set(t))
# # print(set(1))#TypeError: 'int' object is not iterable

# for i in range(260):
#     print(f"{i} - {chr(i)}")
# for i in "test":
#     print(f"{i} - {ord(i)}")

# a = 356
# print(bin(a))
# print(oct(a))
# print(hex(a))


# print("abcd\nefg")
# print("abcd\tefg")
# print("abcd\refg")



# name = "John"
# age = 23
# salary = 999.99
# template = "%s is %d years old. Your sallary is %.3f $ %s"
# print(template)
# print(template % (name, age, salary, name))

# template = "{} is {} years old. Your salary is {:.3f} $"
# print(template.format(name, age, salary))
# template = "{0} is {1} years old. Your salary is {2:.3f} $ {0}"
# print(template.format(name, age, salary))
# template = "{ne} is {ag} years old. Your salary is {sa:.3f} $ {ne}"
# print(template.format(ne=name, ag=age, sa=salary))

# print(f"{name.upper()} is {age} years old. Your salary is {salary**2 :.3f} $")


# text = "SoftServe"

# print(text)
# print(text[0])
# print(text[2])
# print(text[-1])
# # print(text[10])#IndexError: string index out of range
# # print(text[-10])#IndexError: string index out of range
# print(text[1:5])
# print(text[3:])
# print(text[:5])
# print(text[:])
# print(text[::2])
# print(text[2:8:3])
# print(text[::-1])

text = "This will split all words into a list"

print(text.split())
print(text.split("ll"))
print(text.find("ll"))
print(text.find("ll", 8))
print(text.find("ll", 8, 15))# return -1 if not found
print(text.replace("ll", "TEXT"))
l = ["1","2","3","4","5"]
print("=>".join(l))

