def is_perfect_num(num: int):
    result = 0
    for i in range(1, num):
        if num % i == 0:
            result += i

    return num == result


print(is_perfect_num(6))
print(is_perfect_num(28))
print(is_perfect_num(52))
