def greatest_of_three_nums(a: int, b: int, c: int) -> int:
    return max(a, b, c)


def greatest_among_nums(*args):
    return max(list(args))


print(greatest_of_three_nums(100, 150, 120))
print(greatest_among_nums(10, 20, 30, 40, 50, 45, 35))
