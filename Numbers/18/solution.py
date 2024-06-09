def is_prime(num: int):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def prime_factors(num: int):
    result = []
    for i in range(1, num + 1):
        if num % i == 0 and is_prime(i):
            result.append(i)

    return result


print(prime_factors(84))
