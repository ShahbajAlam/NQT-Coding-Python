def is_prime(num: int):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(is_prime(12))
print(is_prime(13))
print(is_prime(17))
