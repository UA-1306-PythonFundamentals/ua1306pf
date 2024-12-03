check, a, b = 1, 1, 1
flag = True

num = int(input("Enter the number: "))
if num == 0:
    flag = False
else:
    while check < num:
        a *= b
        b +=1
        check += 1
    a *= b
if flag == True:
    print(a)
else:
    print("1")

