file = open("lessons\\lesson14\\text.txt")
# print(file.tell())
# print(file.read(14))
# print(file.tell())
# print(">>>"*5)
# print(file.read(5))
# file.seek(3)
# print(">>>"*5)
# print(file.tell())
# print(file.read(5))
# t = ""
# for line in file:
#     t+=line
#     print(line)

# print(t)
# file.close()
# file = open("lessons\\lesson14\\out.txt", "w")

# file.write("test")
# file.write("test")
# file.write("test")
# file.writelines("test")
# file.writelines("test")
# file.close()

with open("lessons\\lesson14\\out.txt", "w") as f:
    for i in range(10):
        f.write(f"{i}\n")
print(f)
f.write(f"99\n")
