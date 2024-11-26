# start = 0
# finish = 10
# while start < finish:
#     print(start)
#     start += 1

# print("The end")


# container = [1, 2, 3, 4, 5, 6, 7]
# # for elenment in 12: pass #TypeError: 'int' object is not iterable
# for elenment in container:
#     print(elenment)
# container = set("hasgdbjhvsbdflj")
# print(container)

# for elenment in container:
#     print(elenment)

# r = range(10)
# print(r)
# print(list(r))
# print(list(range(10)))
# print(list(range(10,20)))
# print(list(range(10,20,3)))
# for i in range(10,20,3):
#     print(i)

# text = "some text"
# # for i in range(len(text)):
# #     print(f"text[{i}]={text[i]}")

# # print(enumerate(text))
# # print(list(enumerate(text)))
# # print(list(enumerate(range(10,20,3))))

# for element in enumerate(text):
#     print(element)

# a, b = 1, 3

# for i, symbol in enumerate(text):
#     print(i, symbol)

# s = 0
# for i in range(20):
#     s += i
#     print(f"{i=} {s=}")
#     if s > 30:
#         break


# print("end")

# number = None
# while not number:
#     x = input("enter number:")
#     if x.isdecimal():
#         number = int(x)
#         break
# print(number)

# values = input("enter data:").split()
# print(values)
# for text in values:
#     if not text.isalnum():
#         break
# else:
#     print("=>".join(values))

# print("end")


values = input("enter data:").split()


s = 0

for text in values:
    print(text, s)
    if not text.isdecimal():
        continue
    s += int(text)
    print("\t", s)
else:
    print("else")

print("end")

for i in range(5):
    pass
