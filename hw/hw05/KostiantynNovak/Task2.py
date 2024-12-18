l = int(input("input range"))
a = int(input("input start"))
b = a
for i in range(l):
     b, a =  a, a + b
     print(a)