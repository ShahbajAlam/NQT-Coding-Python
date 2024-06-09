def factors(num: int):
    result = []

    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)

    return result


print(factors(36))
print(factors(19))
print(factors(63))
