def gcd(a: int, b: int):
    smaller = min(a, b)
    larger = max(a, b)

    if smaller == 0:
        return larger
    return gcd(larger % smaller, smaller)


def gcd_iterative(a: int, b: int):
    smaller = min(a, b)

    while True:
        if a % smaller == 0 and b % smaller == 0:
            break
        else:
            smaller -= 1

    return smaller


print(gcd(96, 128))
print(gcd_iterative(98, 56))
