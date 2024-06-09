import math


def power1(x: int, y: int):
    return x**y


def power2(x: int, y: int):
    return math.pow(x, y)


print(power1(4, 3))
print(power2(4, 3))
