def fib1(n: int):
    if n <= 1:
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)


for i in range(10):
    print(fib1(i), end=" ")


def fib2(n: int):
    result = [0, 1]
    if n == 1:
        return result[:1]
    if n == 2:
        return result
    for _ in range(2, n):
        result.append(result[-1] + result[-2])
    return result


print()
print(fib2(10))
