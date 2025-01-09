import math


def f(a, b, c):
    d = b**2 - 4 * a * c
    if d < 0:
        return "No roots"
    elif d == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        if x1 < x2:
            return x1, x2
        else:
            return x2, x1
