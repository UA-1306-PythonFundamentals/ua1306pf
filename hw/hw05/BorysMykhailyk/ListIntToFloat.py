l = list(range(37))
x=0
# Вивід типу данних в листі до трансформації
while x < len(l):
    print(type(l[x]), l[x])
    x = x +1
# Трансформація з int у float
for i in l:
    i=float(i)
    print(type(i), i)
