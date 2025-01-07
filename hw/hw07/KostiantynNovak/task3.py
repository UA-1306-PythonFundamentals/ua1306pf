def letter_count(a):
    # a = tuple(a)
    b = dict()
    for i in a:
        b[i]=b.get(i,0)+1
    print(a)
    print(b)

# letter_count("hello")

letter_count(str(input("enter anything:")))
