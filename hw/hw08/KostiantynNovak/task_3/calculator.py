from math import pow, pi

def rect_area():
    a = int(input("enter a\n"))
    b = int(input("enter b\n"))
    s = a * b
    return s
def tri_area():
    a = int(input("enter a\n"))
    h = int(input("enter h\n"))
    s = 0.5 * h * a
    return s
def circ_area():
    r = int(input("enter r\n"))
    s = pi * pow(r,2)
    return s
