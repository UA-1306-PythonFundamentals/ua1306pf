a = [] #/2
b = [] #/3
c = [] #!=3 !=2

for num in range(1, 11):
    if num % 2 == 0:
        a.append(num)
    elif num % 3 == 0:
        b.append(num)
    else:
        c.append(num)

print(" / 2:", a)
print(" / 3:", b)
print("not / 2, not / 3:", c)