try:
    a = int(input("enter a num"))+1
    b = 1
    for step in range(1, a):
        b *= step
        print(b)
except:
    print("not a number")

