def gcd(a: int, b: int):
    smaller = min(a, b)
    larger = max(a, b)

    if smaller == 0:
        return larger
    return gcd(larger % smaller, smaller)


def lcm(a, b):
    return (a * b) // gcd(a, b)


print(lcm(15, 20))
