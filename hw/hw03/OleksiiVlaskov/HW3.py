print(f"<{'='*60}>\n<{'='*60}>")
print("Interchange the values ​of two variables without using the third variable.")
print(f"<{'='*60}>\n<{'='*60}>\n\n")

a = 5
b = 2
print(f"{a=}, {b=}")
a, b = b, a
print(f"{a=}, {b=}")

c=6
d=8
print(f"{c=}, {d=}")
d=[c,d]
c=d[1]
d=d[0]
print(f"{c=}, {d=}")

